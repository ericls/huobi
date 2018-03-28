import asyncio
import uuid
import json
import gzip
import aiohttp

from functools import partial


def decode_ws_payload(data):
    return json.loads(gzip.decompress(data).decode('utf-8'))


def encode_ws_payload(data):
    return json.dumps(data)


async def subscribe(topics, on_close=None, on_error=None):
    """
    Please refer to Huobi's documentation for available subscribe channels.

    If callback is not a coroutine function, run_in_executor with default
    Executor will be called.

    Example:
    >>> def btc_callback(data):
            print(data)
    >>> async def eth_callback(data):
            print(data)
    >>> task = subscribe({
            'market.btcusdt.kline.1min': {
                'callback': btc_callback
            },
            'market.ethusdt.kline.1min': {
                'callback': eth_callback
            },
        })
    >>> asyncio.get_event_loop().run_until_complete(task)
    """
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession()
    async with session.ws_connect('wss://api.huobi.pro/ws') as ws:
        keys = {
            topic: uuid.uuid4().hex
            for topic in topics
        }
        keyed_channels = {
            v: topics[k]
            for k, v in keys.items()
        }
        subscribed_chanels = {}
        for topic, config in topics.items():
            payload = {
                'sub': topic,
                'id': keys[topic]
            }
            await ws.send_str(encode_ws_payload(payload))
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.BINARY:
                data = decode_ws_payload(msg.data)

                ping = data.get('ping')
                if ping:
                    reply = encode_ws_payload({'pong': ping})
                    await ws.send_str(
                        reply
                    )

                subbed = data.get('subbed')
                if subbed:
                    if data.get('status') == 'ok':
                        subscribed_chanels[subbed] = keyed_channels[data['id']]

                ch = data.get('ch')
                if ch:
                    cb = subscribed_chanels[ch].get('callback', lambda _: None)
                    if asyncio.iscoroutinefunction(cb):
                        await cb(data)
                    else:
                        loop.run_in_executor(None, partial(cb, data))
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                if on_close:
                    return on_close()
                return
            elif msg.type == aiohttp.WSMsgType.ERROR:
                if on_error:
                    return on_error()
                return
