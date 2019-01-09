import pytest
import json
import pytest
import logging
from models.exchange import Latest, Day, History
from http import HTTPStatus
import allure
import os.path


# def test_latest_foreign():
#     assert Latest().latest_foreign().status_code == HTTPStatus.OK


@pytest.mark.parametrize("inputs", [(Latest().latest_foreign().status_code),
                                    (Latest().latest_base().status_code),
                                    (Latest().latest_sumbols().status_code),
                                    (Day().historical().status_code),
                                    (History().rates_time_period().status_code),
                                    (History().specific_exchange_rates().status_code),
                                    (History().different_currency().status_code)])
def test_status_response(inputs):
    """Check status code is 200"""
    assert inputs == HTTPStatus.OK
    # if inputs == HTTPStatus.OK:
    #     # logging.debug(f"Status code: {inputs}. Something wrong")
    #     print(f"Code status: {inputs}. Successful operation")
