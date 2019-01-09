import pytest
import json
import allure
from models.postcodes import PostCode
from http import HTTPStatus

RANDOM = PostCode().random()


def test_random_status():
    assert RANDOM.status_code == HTTPStatus.OK


def test_random_result():
    assert "postcode" in RANDOM.json()["result"]


@pytest.mark.parametrize('postcodes, status', [('HA5 3WZ', HTTPStatus.OK),
                                               ('', HTTPStatus.BAD_REQUEST),
                                               ("Wrong postcode", HTTPStatus.NOT_FOUND)])
def test_lookup_status(postcodes, status):
    assert PostCode().lookup(postcodes).status_code == status


@pytest.mark.parametrize('postcodes, ', ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"])
def test_lookup_postcodes(postcodes):
    assert PostCode().lookup(postcodes).json()["result"]["postcode"] == postcodes


def test_bulk_lookup():
    data = """{
            "postcodes" : ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"]
                }"""
    assert PostCode().bulk_lookup(data).status_code == HTTPStatus.OK
