"""
Market api tests
"""
import unittest
from huobi.rest.client import HuobiRestClient
from huobi.rest.error import (
    HuobRestiApiError,
    HuobiRestRequstError,
    HuobiRestArgumentError,
)


class TestMarketDataEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = HuobiRestClient(access_key="1", secret_key="2")

    def test_wrong_url(self):
        client = HuobiRestClient(
            access_key="1",
            secret_key="1",
            base_url='https://api.huobi.jfkdlsajfdklsa')
        with self.assertRaises(HuobiRestRequstError):
            client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )


class TestMarketHistoryKline(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_history_kline(
            symbol="btcusdt",
            period="1day",
            size=2
        )

        self.assertEqual(res.res.status_code, 200)
        self.assertEqual(len(res.data['data']), 2)

    def test_wrong_period(self):
        with self.assertRaises(HuobiRestArgumentError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="2day",
                size=2
            )

    def test_wrong_symbol(self):
        with self.assertRaises(HuobRestiApiError):
            self.client.market_history_kline(
                symbol="btcusdt2",
                period="1day",
                size=2
            )

    def test_required_argument(self):
        with self.assertRaises(HuobiRestArgumentError):
            self.client.market_history_kline(
                perioid='1day',
                size=1
            )
