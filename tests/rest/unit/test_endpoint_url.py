
from .cases import MockedTestCase

class TestEndpointUrls(MockedTestCase):

    def test_submit_cancel_order(self):
        # https://github.com/ericls/huobi/issues/1
        self.client.submit_cancel(order_id='1234')
        self.assertIn('/1234/', self.last_url)
        self.client.submit_cancel(order_id='2345')
        self.assertIn('/2345/', self.last_url)
