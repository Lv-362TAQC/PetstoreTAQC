import pytest
import allure
from http import HTTPStatus
from models.user import User


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', ['test', 'user1', 'user2'])
def test_find_user_by_name_positive(inputs):
    assert User._find_user_by_name(inputs).status_code == HTTPStatus.OK


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', ['aerbvtest', 'usqwgbaever1', 'usawebvaewger2'])
def test_find_user_by_name_negative(inputs):
    assert User._find_user_by_name(inputs).status_code == HTTPStatus.INTERNAL_SERVER_ERROR# HTTPStatus.CONFLICT


@allure.step
@allure.story('User')
@pytest.mark.parametrize('inputs', ['test', 'user1', 'user2'])
def test_get_user_by_name_positive(inputs):
    user = User()
    user.get_user_by_name(inputs)
    assert user.username == inputs


@allure.step
@allure.story('User')
def test_get_user_by_name_negative():
    user = User()
    user.get_user_by_name('fcghjbhkbkugyg')
    assert user.username is None
