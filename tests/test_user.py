import pytest
from http import HTTPStatus
from models import user


@pytest.mark.parametrize('inputs', ['test', 'user1', 'user2'])
def test_get_user_by_name_positive(inputs: str) -> None:
    """

    :param inputs:
    :return:
    """
    assert user.User().get_user_by_name(inputs).status_code == HTTPStatus.OK


def test_get_user_by_name_negative() -> None:
    assert user.User().get_user_by_name('qwdqwd').status_code == HTTPStatus.NOT_FOUND
