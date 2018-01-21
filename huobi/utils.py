"""
Helper functions
"""
from typing import Union
from hashlib import sha256
import hmac
import base64

BYTES_OR_STR = Union[
    str,
    bytes,
    bytearray
]


def hmac_sha256_base64(key: BYTES_OR_STR, msg: BYTES_OR_STR,
                       encoding: str = 'utf-8') -> bytes:
    """
    Generate a base64 encoded signature based on secrete key and message
    """
    if isinstance(key, str):
        key = key.encode(encoding)
    if isinstance(msg, str):
        msg = msg.encode(encoding)

    hmac_obj = hmac.new(
        key=key,
        msg=msg,
        digestmod=sha256
    )
    return base64.b64encode(
        hmac_obj.digest()
    )
