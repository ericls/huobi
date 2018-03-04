"""
Market api tests
"""
import unittest
from huobi.rest.client import HuobiRestClient
from huobi.rest.error import (
    HuobiRestiApiError,
    HuobiRestRequestError,
    HuobiRestArgumentError,
)


class TestMarketDataEndpoint(unittest.TestCase):

    def setUp(self):
        self.client = HuobiRestClient()

    def tearDown(self):
        self.client.close()


class TestMarketDataCommon(TestMarketDataEndpoint):

    def test_invalid_url(self):
        client = HuobiRestClient(
            access_key="1",
            secret_key="1",
            base_url='https://api.huobi.jfkdlsajfdklsa')
        with self.assertRaises(HuobiRestRequestError):
            client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )
        client.close()


class TestMarketHistoryKline(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_history_kline(
            symbol="btcusdt",
            period="1day",
            size=2
        )

        self.assertEqual(res.res.status_code, 200)
        self.assertEqual(len(res.data['data']), 2)

    def test_invalid_period(self):
        with self.assertRaises(HuobiRestArgumentError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="2day",
                size=2
            )

    def test_invalid_symbol(self):
        with self.assertRaises(HuobiRestiApiError):
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


class TestMarketDetailMerged(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_detail_merged(symbol='btcusdt')
        self.assertEqual(res.res.status_code, 200)
        self.assertIn('tick', res.data)


class TestMarketDepth(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_depth(symbol='btcusdt')
        self.assertEqual(res.res.status_code, 200)
        self.assertIn('tick', res.data)
        self.assertIn('bids', res.data['tick'])


class TestMarketHistoryTrade(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_history_trade(symbol='btcusdt')
        self.assertEqual(res.res.status_code, 200)
        self.assertEqual(len(res.data['data']), 1)

    def test_invalid_size(self):
        with self.assertRaises(HuobiRestArgumentError):
            self.client.market_history_trade(symbol='btcusdt', size=2002)


class TestMarketDetail(TestMarketDataEndpoint):

    def test_success(self):
        res = self.client.market_detail(symbol='btcusdt')
        self.assertEqual(res.res.status_code, 200)
        self.assertIn('tick', res.data)
        self.assertIn('amount', res.data['tick'])
