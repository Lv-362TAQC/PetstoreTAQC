"""Testing store.py"""
from models.store import Store
from http import HTTPStatus
from models.settings import LOGGER as logger
import pytest
import json


r = Store()


def test_inventory():
    assert r.get_inventory().status_code == HTTPStatus.OK
    assert r.get_inventory().headers['Content-Type'] == 'application/json'


@pytest.mark.parametrize('data', [
        """{"id": 8, "petId": 0, "quantity": 0, "shipDate": "2019-01-03T20:13:27.011Z", "status": "placed", "complete": false}""",
        """{"id": 5, "petId": 5, "quantity": 5, "shipDate": "", "status": "approved", "complete": false}"""
        ])
def test_order(data):
    data_id = json.loads(data)
    r.del_order(data_id['id'])
    assert r.order(data).json() == r.check_order(data_id['id']).json()


def test_order_negative():
    data = """{}"""
    assert r.order(data).text == """{"id":0,"petId":0,"quantity":0,"complete":false}"""


def test_for_wrong_input():
    pass    # wrong json input
