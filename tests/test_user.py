"""Tests for Petstore API."""
import pytest
import allure
from http import HTTPStatus
from models.user import User
from models.settings import USER_USERNAME_VALID, USER_USERNAME_INVALID


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', USER_USERNAME_VALID)
def test_find_user_by_name_positive(inputs):
    assert User._find_user_by_name(inputs).status_code == HTTPStatus.OK


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', USER_USERNAME_INVALID)
def test_find_user_by_name_negative(inputs):
    assert User._find_user_by_name(inputs).status_code == HTTPStatus.CONFLICT  #HTTPStatus.INTERNAL_SERVER_ERROR


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', USER_USERNAME_VALID)
def test_get_user_by_name_set_positive(inputs):
    user = User()
    user.get_user_by_name(inputs)
    assert user.username == inputs


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', USER_USERNAME_INVALID)
def test_get_user_by_name_set_negative(inputs):
    user = User()
    user.get_user_by_name(inputs)
    assert user.username is None
