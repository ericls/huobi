from unittest import TestCase
from huobi import HuobiRestClient


class TestProxies(TestCase):
    def setUp(self):
        self.client = HuobiRestClient(request_params={
            'proxies': {
                'https': 'socks5h://127.0.0.1:1080',
            },
        })

    def test_success(self):
        res = self.client.market_history_kline(
            symbol="btcusdt", period="1day", size=2)

        self.assertEqual(res.res.status_code, 200)
        self.assertEqual(len(res.data['data']), 2)
