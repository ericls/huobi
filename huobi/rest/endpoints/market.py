"""
class of Huobi restful api client, market related endpoints
"""
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


PERIODS = [
    '1min',
    '5min',
    '15min',
    '30min',
    '60min',
    '1day',
    '1mon',
    '1week',
    '1year']


class HuobiRestClientMarket(HuobiRestClientBase):
    """
    Huobi restful api client
    """

    market_history_kline = Endpoint(
        method='get',
        path='/market/history/kline',
        auth_required=False,
        params={
            'symbol': {
                'required': True,
            },
            'period': {
                'default': '5min',
                'choices': [
                    '1min',
                    '5min',
                    '15min',
                    '30min',
                    '60min',
                    '1day',
                    '1mon',
                    '1week',
                    '1year']},
            'size': {
                'default': '1'}})

    market_depth = Endpoint(
        method="get",
        path="/market/depth",
        auth_required=False,
        params={
            'symbol': {
                'required': True
            },
            'type': {
                'required': True,
                'default': 'step0',
                'choices': [f'step{i}' for i in range(0, 6)]
            }
        }
    )

    market_detail_merged = Endpoint(
        method='get',
        path="/market/detail/merged",
        auth_required=False,
        params={
            'symbol': {
                'required': True
            }
        }
    )

    market_history_trade = Endpoint(
        method='get',
        path='/market/history/trade',
        auth_required=False,
        params={
            'symbol': {
                'required': True
            },
            'size': {
                'default': 1,
                'choices': list(range(1, 2001))
            }
        }
    )

    market_detail = Endpoint(
        method='GET',
        path='/market/detail',
        auth_required=False,
        params={
            'symbol': {
                'required': True
            }
        }
    )
