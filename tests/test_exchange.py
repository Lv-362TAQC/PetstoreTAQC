"""Tests for foreign exchange rates API with currency conversion"""

import pytest
from tests.data import *
from models.exchange import Latest, Day, History
from http import HTTPStatus


def test_latest_foreign():
    """Testing method for check response code"""
    assert Latest().latest_foreign().status_code == HTTPStatus.OK


def test_latest_foreign_hrk():
    """Testing method for check value"""
    assert 7.4281 == Latest().latest_foreign().json()["rates"]["HRK"]


@pytest.mark.parametrize("inputs", [data_latest])
def test_latest_foreign_response(inputs):
    """Testing method for check latest foreign response"""
    assert inputs == Latest().latest_foreign().json()


def test_latest_base():
    """Testing method for check response code"""
    assert Latest().latest_base().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_usd])
def test_latest_base_response(inputs):
    """Testing method for check latest base response"""
    assert inputs == Latest().latest_base().json()


def test_latest_symbols():
    """Testing method for check response code"""
    assert Latest().latest_symbols().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_usd_gbp])
def test_latest_symbols_response(inputs):
    """Testing method for check latest symbols response"""
    assert inputs == Latest().latest_symbols().json()


def test_historical():
    """Testing method for check response code"""
    assert Day().historical().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_day])
def test_history(inputs):
    """Testing method for check history day response"""
    assert inputs == Day().historical().json()


def test_rates_time_period():
    """Testing method for check response code"""
    assert History().rates_time_period().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_rates])
def test_history_resp(inputs):
    """Testing method for rates time period response"""
    assert inputs == History().rates_time_period().json()


def test_specific_exchange_rates():
    """Testing method for check response code"""
    assert History().specific_exchange_rates().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_specific])
def test_spec_exchange(inputs):
    """Testing method for specific exchange rates"""
    assert inputs == History().specific_exchange_rates().json()


def test_different_currency():
    """Testing method for check response code"""
    assert History().different_currency().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [data_diff_currency])
def test_diff_currency(inputs):
    """Testing method for specific exchange rates"""
    assert inputs == History().different_currency().json()
