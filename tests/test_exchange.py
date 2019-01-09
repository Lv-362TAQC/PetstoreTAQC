import pytest
import json
import pytest
import logging
from exchange_model.exchange import Latest, Day, History
from http import HTTPStatus
import allure
import os.path


def test_latest_foreign():
    assert Latest().latest_foreign().status_code == HTTPStatus.OK


def test_latest_base():
    assert Latest().latest_base().status_code == HTTPStatus.OK


def test_latest_symbols():
    assert Latest().latest_symbols().status_code == HTTPStatus.OK


def test_historical():
    assert Day().historical().status_code == HTTPStatus.OK


def test_rates_time_period():
    assert History().rates_time_period().status_code == HTTPStatus.OK


def test_specific_exchange_rates():
    assert History().specific_exchange_rates().status_code == HTTPStatus.OK


def test_different_currency():
    assert History().different_currency().status_code == HTTPStatus.OK


# @pytest.mark.parametrize("inputs", [(Latest().latest_foreign().status_code),
#                                     (Latest().latest_base().status_code),
#                                     (Latest().latest_sumbols().status_code),
#                                     (Day().historical().status_code),
#                                     (History().rates_time_period().status_code),
#                                     (History().specific_exchange_rates().status_code),
#                                     (History().different_currency().status_code)])
# def test_status_response(inputs):
#     """Check status code is 200"""
#     assert inputs == HTTPStatus.OK
#     # if inputs == HTTPStatus.OK:
#     #     # logging.debug(f"Status code: {inputs}. Something wrong")
#     #     print(f"Code status: {inputs}. Successful operation")
