"""
class of Huobi restful api client
"""
from huobi.rest.endpoints.common import HuobiRestClientCommon
from huobi.rest.endpoints.market import HuobiRestClientMarket
from huobi.rest.endpoints.account import HuobiRestClientAccounts
from huobi.rest.endpoints.order import HuobiRestClientOrder


class HuobiRestClient(
    HuobiRestClientMarket,
    HuobiRestClientCommon,
    HuobiRestClientAccounts,
    HuobiRestClientOrder,
):
    """
    Huobi restful api client
    """
    pass
