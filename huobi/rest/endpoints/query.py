
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientQuery(HuobiRestClientBase):
    deposit_withdraw = Endpoint(
        method='GET',
        path='/v1/query/deposit-withdraw',
        params={
            'currency': {
                'required': True
            },
            'type': {
                'required': True,
                'choices': ['deposit', 'withdraw']
            },
            'from': {
                'default': 0,
            },
            'size': {
                'default': 100,
            }
        }
    )