import inspect
from unittest import TestCase
from huobi import HuobiRestClient


class TestSignature(TestCase):

    def setUp(self):
        self.client = HuobiRestClient()

    def test_has_signature(self):
        signature = inspect.signature(self.client.market_history_kline)
        assert all(i in signature.parameters for i in ['size', 'period', 'symbol'])
