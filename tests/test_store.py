"""Testing store.py"""
from models.store import Store
from http import HTTPStatus
from models.logger import logger
import pytest
import json


r = Store()


def test_inventory():
    assert r.get_inventory().status_code == HTTPStatus.OK
    assert r.get_inventory().headers['Content-Type'] == 'application/json'


@pytest.mark.parametrize('data', [
        """{"id": 8, "petId": 0, "quantity": 0, "shipDate": "2019-01-03T20:13:27.011Z",
        "status": "placed", "complete": false}""",
        """{"id": 5, "petId": 5, "quantity": 5, "shipDate": "",
                "status": "approved", "complete": false}"""
        ])
def test_order(data):
    data_id = json.loads(data)
    if 'id' in data_id:
        r.del_order(data_id['id'])
        assert r.order(data).json() == r.check_order(data_id['id']).json()
    else:
        assert r.order(data).json() == r.check_order(0).json()


def test_order_negative():
    data = """{}"""
    try:
        data_id = json.loads(data)
        r.order(data)
        assert r.check_order(data_id).status_code == 404
    except KeyError:
        logger.exception(f"Key error: input = {data}")
