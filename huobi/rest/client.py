"""
class of Huobi restful api client
"""
from requests import Session

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


class HuobiRestClient(object):
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

    def __init__(self, access_key, secret_key,

                 base_url='https://api.huobi.pro'):
        self.access_key = access_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.session = Session()
