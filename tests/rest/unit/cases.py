import json
from unittest import TestCase, mock
from huobi import HuobiRestClient


class MockedTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mocked_response = {'status': 'ok', 'data': {}}
        self.mocked_response_status_code = 200

    def setUp(self):
        access_key = 'foo'
        secret_key = 'bar'
        self.client = HuobiRestClient(
            access_key=access_key, secret_key=secret_key
        )
        self.client.session = self._get_mock_session()
        self.history = {}
        self.last_url = ''

    def tearDown(self):
        self.client.close()
    
    def _get_mock_session(self):

        def raise_exception():
            raise Exception()

        def mocked_request_method(url='', **kwargs):
            url = url or kwargs.get('url')
            self.last_url = url
            self.history[url] = kwargs
            response = mock.Mock()
            response.raise_for_status = mock.Mock()
            if self.mocked_response_status_code > 300:
                response.raise_for_status.side_effect = raise_exception
            response.status_code = self.mocked_response_status_code
            response.json = mock.Mock()
            response.json.return_value = self.mocked_response
            return response

        session = mock.Mock()
        session.post = session.get = request_method = mock.Mock()
        request_method.side_effect = mocked_request_method
        return session
