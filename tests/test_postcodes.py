import pytest
import json
from models.postcodes import PostCode
from http import HTTPStatus


def test_random():
    random = PostCode().random()
    assert random.status_code == HTTPStatus.OK
    assert "result" in random.json()
    assert "postcode" in random.json()["result"]


def test_lookup():
    assert PostCode().lookup("OX49 5NU").status_code == HTTPStatus.OK
    assert PostCode().lookup("").status_code == HTTPStatus.BAD_REQUEST
    assert PostCode().lookup("Wrong postcode").status_code == HTTPStatus.NOT_FOUND
    assert "result" in PostCode().lookup("OX49 5NU").json()
    assert PostCode().lookup("OX49 5NU").json()["result"]["postcode"] == "OX49 5NU"


def test_bulk_lookup():
    data = """{
            "postcodes" : ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"]
                }"""
    assert PostCode().bulk_lookup(data).status_code == HTTPStatus.OK