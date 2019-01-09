""" GET. Find purchase order by ID. For valid response try integer IDs with
    value >= 1 and <= 10. Other values will generated exceptions.
    DELETE. Delete purchase order by ID.For valid response
    try integer IDs with positive integer value.
    Negative or non-integer values will generate API errors. """

import json
from http import HTTPStatus
import pytest
import requests
from models.store_get_delete import Store


BASE_URL = "https://petstore.swagger.io/v2/store/order/"

S = Store()


@pytest.mark.parametrize('order_id, output', [(-5, 404), (0, 404), (1, 200),
                                              (2, 200), (3, 200), (4, 200), (5, 200),
                                              (6, 200), (7, 200), (8, 200), (9, 200),
                                              (10, 200), (11, 404), (20, 404)])
def test_get(order_id, output):
    """checking store_get func"""
    assert S.storeget(order_id).status_code == output


# POST data before DELETE.
DATA_JSON = json.loads("""{
  "id": 13,
  "petId": 123,
  "quantity": 1,
  "shipDate": "2018-12-31T08:23:29.842Z",
  "status": "placed",
  "complete": false
}""")
requests.post(BASE_URL, json=DATA_JSON)
# DELETE data.
DEL_ID = 13
S.storedelete(DEL_ID)


def test_del():
    """checking order id for 404 status."""
    assert requests.get(BASE_URL + str(DEL_ID)).status_code == HTTPStatus.NOT_FOUND
