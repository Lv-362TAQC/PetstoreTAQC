"""Testing store.py"""

import pytest
import json
from models.store import Store

r = Store()


def test_inventory():
    assert r.get_inventory().status_code == 200
    assert r.get_inventory().headers['Content-Type'] == 'application/json'


def test_order():
    order_id = '8'
    data = """{
      "id": 8,
      "petId": 0,
      "quantity": 0,
      "shipDate": "2019-01-03T20:13:27.011Z",
      "status": "placed",
      "complete": false}"""

    r.del_order(order_id)
    assert r.order(data) == r.check_order(order_id)

    # assert test.status_code != 404
    # assert test.json()['message'] != 'Order not found'
