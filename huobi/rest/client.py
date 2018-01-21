"""
class of Huobi restful api client
"""
from huobi.rest.endpoints.common import HuobiRestClientCommon
from huobi.rest.endpoints.market import HuobiRestClientMarket
from huobi.rest.endpoints.account import HuobiRestClientAccounts


class HuobiRestClient(
    HuobiRestClientMarket,
    HuobiRestClientCommon,
    HuobiRestClientAccounts
):
    """
    Huobi restful api client
    """
    pass
