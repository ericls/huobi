import inspect
from urllib.parse import parse_qs, urlparse
from huobi.rest.error import HuobiRestiApiError, HuobiRestRequestError
from .cases import MockedTestCase


class TestEndpoint(MockedTestCase):
    """
    tests for Endpoint
    """

    def test_submit_cancel_order(self):
        # https://github.com/ericls/huobi/issues/1
        self.client.submit_cancel(order_id='1234')
        self.assertIn('/1234/', self.last_url)
        self.client.submit_cancel(order_id='2345')
        self.assertIn('/2345/', self.last_url)

    def test_none_param_value(self):
        # https://github.com/ericls/huobi/issues/4
        # The idea is that if a value to a param if None, instead of include a None value in the request,
        # just don't include it in the request parameters
        self.client.orders(symbol='xrpusdt', states='submitted')
        url = urlparse(self.last_url)
        query = url.query
        qs = parse_qs(query)
        self.assertNotIn('types', qs)
        self.assertNotIn('direct', qs)

    def test_has_signature(self):
        signature = inspect.signature(self.client.market_history_kline)
        assert all(i in signature.parameters for i in ['size', 'period', 'symbol'])

    def test_400(self):
        # 400 series is client side error. Server will likely return helpful error message
        # Do not throw Request Error, throw ApiError instead
        self.mocked_response_status_code = 403
        self.mocked_response = {'status': 'error', 'err-code': 1, 'err-message': 'test'}
        with self.assertRaises(HuobiRestiApiError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )

    def test_500(self):
        self.mocked_response_status_code = 500
        with self.assertRaises(HuobiRestRequestError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )
