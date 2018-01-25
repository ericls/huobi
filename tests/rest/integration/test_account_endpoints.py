import unittest
from huobi.rest.client import HuobiRestClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(dirname(dirname(dirname(__file__)))), '.env')
load_dotenv(dotenv_path)


class TestAccountEndpoint(unittest.TestCase):

    def setUp(self):
        access_key = os.environ['ACCESS_KEY']
        secret_key = os.environ['SECRET_KEY']
        self.client = HuobiRestClient(
            access_key=access_key, secret_key=secret_key)

    def tearDown(self):
        self.client.close()


class TestAccountAccounts(TestAccountEndpoint):

    def test_success(self):
        res = self.client.accounts()
        self.assertEqual(res.res.status_code, 200)


class TestAccountBalance(TestAccountEndpoint):

    def test_success(self):
        account_id = self.client.accounts().data['data'][0]['id']
        res = self.client.balance(account_id=account_id)
        self.assertEqual(res.res.status_code, 200)
