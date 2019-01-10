""" GET. Find purchase order by ID. For valid response try integer IDs with
    value >= 1 and <= 10. Other values will generated exceptions.
    DELETE. Delete purchase order by ID.For valid response
    try integer IDs with positive integer value.
    Negative or non-integer values will generate API errors. """

import json
from http import HTTPStatus
import pytest
import requests
from models.store_get_del import Store
from models.settings import BASE_URL_ORD, DATA_JSON


S = Store()


@pytest.mark.parametrize('order_id', [1, 2, 4, 5, 6, 7, 9, 10])
def test_get_pos(order_id):
    """checking store_get func"""
    assert S.storeget(order_id).status_code == HTTPStatus.OK


@pytest.mark.parametrize('order_id', [-5, 0, 11, 20])
def test_get_neg(order_id):
    """checking store_get func"""
    assert S.storeget(order_id).status_code == HTTPStatus.NOT_FOUND


requests.post(BASE_URL_ORD, json=DATA_JSON)

# DELETE data.
DEL_ID = 3
S.storedelete(DEL_ID)


def test_del():
    """checking order id for 404 status."""
    assert S.storeget(DEL_ID).status_code == HTTPStatus.NOT_FOUND
