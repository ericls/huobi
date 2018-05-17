from huobi.rest.error import HuobiRestiApiError, HuobiRestRequestError
from .cases import MockedTestCase


class TestHandleResponse(MockedTestCase):

    def test_400(self):
        # 400 series is client side error. Server will likely return helpful error message
        # Do not thorw Request Error, throw ApiError instead
        self.mocked_respnse_status_code = 403
        self.mocked_respnse = {'status': 'error', 'err-code': 1, 'err-message': 'test'}
        with self.assertRaises(HuobiRestiApiError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )


    def test_500(self):
        self.mocked_respnse_status_code = 500
        with self.assertRaises(HuobiRestRequestError):
            self.client.market_history_kline(
                symbol="btcusdt",
                period="1day",
                size=2
            )