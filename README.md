# Huobi

Huobi Python SDK

## Requirements
```bash
Python>=3.6
```

## Installaton
```bash
pip install huobi
```

## Usage
### Rest API
Example: 
```python
>>> from huobi import HuobiRestClient
>>> client = HuobiRestClient(access_key=..., secret_key=...)
>>> trades = client.market_history_trade(symbol='ethusdt').data
```
To see all available methods and their arguments:
```python
>>> from huobi import HuobiRestClient
>>> help(HuobiRestClient)
>>> help(HuobiRestClient.symbols)
```

### Real Time API

> Rudimentary websocket subscription support

Please refer to Huobi's documentation for available subscribe channels.

If callback is not a coroutine function, run_in_executor with default
Executor will be called.

Example:
```python
from huobi import subscribe
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
```