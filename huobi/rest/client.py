"""
class of Huobi restful api client
"""
from huobi.rest.endpoints.common import HuobiRestClientCommon
from huobi.rest.endpoints.market import HuobiRestClientMarket
from huobi.rest.endpoints.account import HuobiRestClientAccounts
from huobi.rest.endpoints.order import HuobiRestClientOrder
from huobi.rest.endpoints.query import HuobiRestClientQuery


class HuobiRestClient(
    HuobiRestClientMarket,
    HuobiRestClientCommon,
    HuobiRestClientAccounts,
    HuobiRestClientOrder,
    HuobiRestClientQuery,
):
    """
    Huobi restful api client
    """
    pass
