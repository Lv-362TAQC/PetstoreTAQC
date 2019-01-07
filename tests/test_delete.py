"""DELETE  Delete purchase order by ID.For valid response
        try integer IDs with positive integer value.
        Negative or non-integer values will generate API errors """
import pytest
from store_delete import Store

S = Store()


@pytest.mark.parametrize('data, del_id, get_value', [("""{
                                                      "id": 16,
                                                      "petId": 123,
                                                      "quantity": 1,
                                                      "shipDate": "2018-12-31T08:23:29.842Z",
                                                      "status": "placed",
                                                      "complete": false
                                                      }""", 16, 404),
                                                     ("""{
                                                      "id": 22,
                                                      "petId": 123,
                                                      "quantity": 1,
                                                      "shipDate": "2018-12-31T08:23:29.842Z",
                                                      "status": "placed",
                                                      "complete": false
                                                       }""", 22, 404)])
def test_gets(data, del_id, get_value):
    """checking storedelete func"""
    assert S.storedelete(data, del_id).status_code == get_value
