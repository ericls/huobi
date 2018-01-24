"""
class of Huobi restful api client, account related endpoints
"""
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientAccounts(HuobiRestClientBase):
    """
    Huobi restful api client
    """

    accounts = Endpoint(
        method='GET',
        path='/v1/account/accounts',
        auth_required=True,
    )

    balance = Endpoint(
        method='GET',
        path='/v1/account/accounts/{account-id}/balance',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'url': 'account-id'
            }
        }
    )
