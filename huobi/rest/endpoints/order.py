"""
class of Huobi restful api client, order related endpoints
"""
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientOrder(HuobiRestClientBase):

    place = Endpoint(
        method='POST',
        path='/v1/order/orders/place',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'name': 'account-id'
            },
            'amount': {
                'required': True,
            },
            'price': {
                'required': False,
            },
            'source': {
                'required': False,
            },
            'symbol': {
                'required': True
            },
            'type': {
                'required': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                ]
            },
        }
    )

    submit_cancel = Endpoint(
        method='POST',
        path='/v1/order/orders/{order-id}/submitcancel',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    batch_cancel = Endpoint(
        method='POST',
        path='/v1/order/orders/batchcancel',
        auth_required=True,
        params={
            'order_ids': {
                'required': True,
                'name': 'order-ids',
                'type': list
            }
        }
    )

    status = Endpoint(
        method='GEt',
        path='/v1/order/orders/{order-id}',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    matchresults = Endpoint(
        method='GEt',
        path='/v1/order/orders/{order-id}',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )


