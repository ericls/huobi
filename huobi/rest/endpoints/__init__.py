"""
class of Huobi restful api client
"""
from requests import Session
from huobi.rest.endpoint import Endpoint


class HuobiRestClientBaseMeta(type):
    def __new__(mcls, name, bases, attrs):
        cls = super(
            HuobiRestClientBaseMeta,
            mcls).__new__(
            mcls,
            name,
            bases,
            attrs)
        for attr, obj in attrs.items():
            if isinstance(obj, Endpoint):
                obj.__set_name__(cls, attr)
        return cls


class HuobiRestClientBase(object, metaclass=HuobiRestClientBaseMeta):
    """
    Huobi restful api client base
    """

    def __init__(
            self,
            access_key=None,
            secret_key=None,
            base_url='https://api.huobi.pro'):
        self.access_key = access_key
        self.secret_key = secret_key
        self.base_url = base_url
        with Session() as session:
            self.session = session

    def close(self):
        self.session.close()
