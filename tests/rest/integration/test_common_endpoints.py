import unittest
from huobi.rest.client import HuobiRestClient
from huobi.rest.error import (
    HuobiRestiApiError
)

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(dirname(dirname(dirname(__file__)))), '.env')
load_dotenv(dotenv_path)


class TestCommonEndpoint(unittest.TestCase):

    def setUp(self):
        access_key = os.environ['ACCESS_KEY']
        secret_key = os.environ['SECRET_KEY']
        self.client = HuobiRestClient(
            access_key=access_key, secret_key=secret_key)

    def tearDown(self):
        self.client.close()


class TestCommonSymbols(TestCommonEndpoint):

    def test_success(self):
        res = self.client.symbols()
        self.assertEqual(res.res.status_code, 200)
        self.assertIn('data', res.data)
        self.assertIsInstance(res.data['data'], list)

    def test_authentication_fail(self):
        client = HuobiRestClient(
            access_key='1',
            secret_key='2',
        )
        with self.assertRaises(HuobiRestiApiError):
            client.accounts()


class TestCommonCurrencies(TestCommonEndpoint):

    def test_success(self):
        res = self.client.currencies()
        self.assertEqual(res.res.status_code, 200)

    def test_alias(self):
        res = self.client.currencys()
        self.assertEqual(res.res.status_code, 200)


class TestCommonTimestamp(TestCommonEndpoint):

    def test_success(self):
        res = self.client.timestamp()
        self.assertEqual(res.res.status_code, 200)
