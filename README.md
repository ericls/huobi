# Huobi

Huobi Python SDK
## Requirements
```conf
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
>>> from huobi.rest.client import HuobiRestClient
>>> client = HuobiRestClient(access_key=..., secret_key=...)
>>> tades = client.market_history_trade(symbol='ethusdt').data
```
To see all available methods and their arguments:
```
>>> from huobi.rest.client import HuobiRestClient
>>> help(HuobiRestClient)
>>> help(HuobiRestClient.symbols)
```

### Real Time API
```
NotImplemented
```