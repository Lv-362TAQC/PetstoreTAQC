"""Testing of PostCodes API."""
from http import HTTPStatus
import pytest
from models.postcodes import PostCode

RANDOM = PostCode().random()


def test_random_status():
    """Testing method of getting random postcode."""
    assert RANDOM.status_code == HTTPStatus.OK


def test_random_result():
    """Testing method of getting random postcode."""
    assert "postcode" in RANDOM.json()["result"]


@pytest.mark.parametrize('postcodes, status', [('HA5 3WZ', HTTPStatus.OK),
                                               ('', HTTPStatus.BAD_REQUEST),
                                               ("Wrong postcode", HTTPStatus.NOT_FOUND)])
def test_lookup_status(postcodes, status):
    """Testing method of getting info by given postcode."""
    assert PostCode().lookup(postcodes).status_code == status


@pytest.mark.parametrize('postcodes, ', ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"])
def test_lookup_postcodes(postcodes):
    """Testing method of getting info by given postcode."""
    assert PostCode().lookup(postcodes).json()["result"]["postcode"] == postcodes


def test_bulk_lookup():
    """Testing method of getting info by given postcodes in json."""
    data = """{
            "postcodes" : ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"]
                }"""
    assert PostCode().bulk_lookup(data).status_code == HTTPStatus.OK
