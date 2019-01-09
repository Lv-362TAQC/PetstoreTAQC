"""Testing store.py"""
from models.store import Store
from http import HTTPStatus
import pytest
import json
import allure
from models.settings import STORE_TEST_DATA, STORE_EMPTY_DATA, STORE_DEFAULT

r = Store()

@allure.step
def test_inventory():
    with allure.step("Check status code of inventory request."):
        assert r.get_inventory().status_code == HTTPStatus.OK
    with allure.step("Check content type of inventory request."):
        assert r.get_inventory().headers['Content-Type'] == 'application/json'

@allure.step
@pytest.mark.parametrize('data', STORE_TEST_DATA)
def test_order(data):
    data_id = json.loads(data)
    with allure.step("Prematurely delete order id that we are testing."):
        r.del_order(data_id['id'])
    with allure.step("Check if order with given id was placed."):
        assert r.order(data).json() == r.check_order(data_id['id']).json()

@allure.step
def test_order_empty():
    with allure.step("Check if server returns default response when it receives empty json input."):
        assert r.order(STORE_EMPTY_DATA).text == STORE_DEFAULT

@allure.step
def test_for_wrong_input():
    pass    # wrong json input
