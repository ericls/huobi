import unittest
import os
from huobi.rest.client import HuobiRestClient
from huobi.rest.error import HuobiRestiApiError

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(dirname(dirname(dirname(__file__)))), '.env')
load_dotenv(dotenv_path)


class TestOrderEndpoints(unittest.TestCase):

    def setUp(self):
        access_key = os.environ['ACCESS_KEY']
        secret_key = os.environ['SECRET_KEY']
        self.client = HuobiRestClient(
            access_key=access_key, secret_key=secret_key
        )

    def tearDown(self):
        self.client.close()


class TestOrdersE2E(TestOrderEndpoints):

    def test_end_to_end(self):
        # TODO: need mock server to to this integration test
        # place order
        account_id = self.client.accounts().data['data'][0]['id']
        with self.assertRaises(HuobiRestiApiError):
            self.client.place(
                account_id=account_id,
                symbol='btcusdt',
                amount='1',
                price='1',
                type='buy-limit'
            )
