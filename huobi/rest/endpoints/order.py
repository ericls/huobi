"""
class of Huobi restful api client, order related endpoints
"""
import datetime
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


def date_formatter(d):
    if isinstance(d, datetime.datetime):
        return d.date().isoformat()
    if isinstance(d, datetime.date):
        return d.isoformat()
    if isinstance(d, str):
        return d


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
        method='GET',
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
        method='GET',
        path='/v1/order/orders/{order-id}',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    orders = list_orders = Endpoint(
        method='GET',
        path='/v1/order/orders',
        auth_required=True,
        params={
            'symbol': {
                'required': True,
            },
            'types': {
                'required': False,
                'multiple': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                ]
            },
            'start_date': {
                'required': False,
                'formatter': date_formatter
            },
            'end_date': {
                'required': False,
                'formatter': date_formatter
            },
            'states': {
                'required': True,
                'choices': [
                    'pre-submitted',
                    'submitted',
                    'partial-filled',
                    'partial-canceled',
                    'filled',
                    'canceled',
                ]
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ]
            },
            'size': {
                'required': False,
            }
        }
    )

    list_matchresults = Endpoint(
        method='GET',
        path='/v1/order/matchresults',
        auth_required=True,
        params={
            'symbol': {
                'required': True,
            },
            'types': {
                'required': False,
                'multiple': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                ]
            },
            'start_date': {
                'required': False,
                'formatter': date_formatter
            },
            'end_date': {
                'required': False,
                'formatter': date_formatter
            },
            'states': {
                'required': True,
                'choices': [
                    'pre-submitted',
                    'submitted',
                    'partial-filled',
                    'partial-canceled',
                    'filled',
                    'canceled',
                ]
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ]
            },
            'size': {
                'required': False,
            }
        }
    )
