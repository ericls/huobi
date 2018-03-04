"""
Error classes
"""


class HuobiRestError(Exception):
    """
    Huobi rest client exceptions
    """
    pass


class HuobiRestRequestError(HuobiRestError):
    """
    Huobi rest client request exceptions
    """
    pass


class HuobiRestiApiError(HuobiRestError):
    """
    Huobi server returned errors
    """
    pass


class HuobiRestApiDecodeError(HuobiRestError):
    """
    Whatever returned from api is not json
    """
    pass


class HuobiRestArgumentError(HuobiRestError):
    """
    Argument related errors
    """
    pass
