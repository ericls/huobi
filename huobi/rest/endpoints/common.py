"""
class of Huobi restful api client, common endpoints
"""
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientCommon(HuobiRestClientBase):
    """
    Huobi restful api client
    """

    symbols = Endpoint(
        method='GET',
        path='/v1/common/symbols',
        auth_required=False,
    )

    currencys = currencies = Endpoint(
        method='GET',
        path='/v1/common/currencys'
    )

    timestamp = Endpoint(
        method='GET',
        path='/v1/common/timestamp',
        auth_required=False,
    )
