""" Endpoint and HuobiRestResult class
"""
from datetime import datetime
from urllib.parse import urlparse, parse_qsl, urlencode
from inspect import Signature, Parameter

from huobi.rest.helper import REQUIRED_HEADERS, REQUIRED_POST_HEADERS
from huobi.rest.error import (
    HuobiRestError,
    HuobiRestRequestError,
    HuobiRestiApiError,
    HuobiRestArgumentError,
    HuobiRestApiDecodeError
)
from huobi.utils import hmac_sha256_base64


class HuobiRestEndpointResult(object):
    """
    Huobi Rest Endpoint Result
    """

    def __init__(self, req, res, data):
        self.req = req
        self.res = res
        self.data = data


class Endpoint(object):
    """
    Endpoint class
    """

    def __init__(
            self,
            method,
            path,
            params=None,
            auth_required=True,
    ):
        self.method = method
        self.path = path
        self.auth_required = auth_required
        self.params = params or {}
        self.attr_name = None

    def __set_name__(self, _owner, name):
        self.attr_name = name

    def _sign_url(self, instance, method: str, url: str):
        if not self.auth_required:
            return url
        additional_qs = {
            'SignatureMethod': 'HmacSHA256',
            'SignatureVersion': '2',
            'Timestamp': datetime.utcnow().isoformat(timespec='seconds'),
            'AccessKeyId': instance.access_key,
        }
        url_obj = urlparse(url)
        qs_items = parse_qsl(url_obj.query) + list(additional_qs.items())
        qs_string = urlencode(sorted(qs_items))
        msg = (
            f'{method.upper()}\n'
            f'{url_obj.netloc}\n'
            f'{url_obj.path}\n'
            f'{qs_string}'
        ).strip()
        signature = hmac_sha256_base64(instance.secret_key, msg)
        new_qs_dict = {**dict(qs_items), 'Signature': signature}
        new_url = (
            f'{url_obj.scheme}://{url_obj.netloc}'
            f'{url_obj.path}?{urlencode(new_qs_dict)}'
        )
        return new_url

    @staticmethod
    def _generate_param_docs(param_name, param_config):
        choices = param_config.get('choices', [])
        if len(choices) > 20:
            start = ",".join(map(str, choices[:10]))
            end = ",".join(map(str, choices[-10:]))
            choices = f'[{start},...,{end}]'
        lines = [
            f'  * *{param_name}*',
            f'      this keyword argument takes a list of values \n' if param_config.get('multiple') else '',
            f'      :required by Huobi: {param_config.get("required", False)}',
            f"      :default: {param_config['default']}" if 'default' in param_config else '',
            f"      :choices: {choices}" if 'choices' in param_config else '',
        ]
        return '\n'.join([line for line in lines if line])

    def _generate_docs(self):
        param_docs = '\n'.join([
            self._generate_param_docs(k, v)
            for k, v in self.params.items()
        ])
        doc = [
            ":param \**kwargs:\n  See blow\n :Keyword Arguments:"
            if self.params else "This method does not require arguments",
            f'{param_docs}',
        ]
        return '\n'.join(doc)

    @staticmethod
    def _handle_response(_instance, res):
        try:
            if res.status_code >= 500:
                res.raise_for_status()
        except Exception as exc:
            raise HuobiRestRequestError('Request Error') from exc
        try:
            json_data = res.json()
        except Exception as exc:
            raise HuobiRestApiDecodeError('Json decode error') from exc

        if not json_data.get('status') == 'ok':
            error_code = json_data.get('err-code', 'Unknown error code')
            error_msg = json_data.get('err-msg', 'Unknown error message')
            raise HuobiRestiApiError(
                f'{error_code}: {error_msg} \n'
                f'{res.request.method}: {res.request.url}'
            )

        return HuobiRestEndpointResult(res.request, res, json_data)

    def _get_signature(self):
        parameters = []
        for param_name, param_spec in self.params.items():
            param = Parameter(
                name=param_name,
                kind=Parameter.KEYWORD_ONLY,
                default=(param_spec.get('default') or Parameter.empty) if param_spec.get('required') else None,
            )
            parameters.append(param)
        return Signature(parameters=parameters)

    def _with_signature(self, func):
        func.__signature__ = self._get_signature()
        return func

    def __get__(self, instance, owner):

        @self._with_signature
        def _wrapper(**kwargs):
            if self.auth_required and (
                    not instance.secret_key or not instance.access_key):
                raise HuobiRestError(
                    f'Authentication is required for method: {self.attr_name}')
            query_params = {}
            path = self.path
            for param_name, param_spec in self.params.items():
                required = param_spec.get('required', False)
                choices = param_spec.get('choices', None)
                multiple = param_spec.get('multiple', False)
                if required and (
                        'default' not in param_spec
                ) and not kwargs.get(param_name):
                    raise HuobiRestArgumentError(
                        f'{param_name} is required in {self.attr_name}'
                    )
                param_value = kwargs.get(
                    param_name,
                    param_spec.get('default')
                )
                formatter = param_spec.get('formatter')
                if formatter:
                    param_value = formatter(param_value)
                if choices and param_value:
                    if param_value not in choices and not multiple:
                        raise HuobiRestArgumentError(
                            f'{param_value} is not a'
                            f'valid value for {param_name} \n'
                            f'Choices are {choices}')
                    if multiple and not all([part in choices for part in param_value.split(',')]):
                        raise HuobiRestArgumentError(
                            f'{param_value} contains'
                            f'invalid value for {param_name} \n'
                            f'Choices are {choices}')
                required_type = param_spec.get('type')
                if required_type and not isinstance(param_value, required_type):
                    raise HuobiRestArgumentError(
                        f'{param_name} should be of instance of {required_type}'
                        f'but got {type(param_name)}'
                    )
                if param_value is not None:
                    url_replace = param_spec.get('url')
                    if url_replace:
                        path = path.replace(
                            '{' + url_replace + '}', str(param_value)
                        )
                    else:
                        name = param_spec.get('name', param_name)
                        query_params[name] = param_value

            url = f'{instance.base_url}{path}'
            res = None
            if self.method.lower() == 'get':
                url = f'{url}?{urlencode(query_params)}'
                url = self._sign_url(instance, 'GET', url)
                try:
                    res = instance.session.get(url, headers=REQUIRED_HEADERS)
                except Exception as exc:
                    raise HuobiRestRequestError('Request error') from exc
            if self.method.lower() == 'post':
                url = self._sign_url(instance, 'POST', url)
                try:
                    res = instance.session.post(
                        url,
                        json=query_params,
                        headers=REQUIRED_POST_HEADERS
                    )
                except Exception as exc:
                    raise HuobiRestRequestError('Request error') from exc

            return self._handle_response(instance, res)

        _wrapper.__name__ = self.attr_name
        _wrapper.__doc__ = self._generate_docs()

        return _wrapper
