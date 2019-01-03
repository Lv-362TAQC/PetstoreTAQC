import pytest
from models import user


@pytest.mark.parametrize('inputs, outputs', [
    ('test', 200),
    ('user1', 200),
    ('user2', 200),
])
def test_get_user_by_name_positive(inputs, outputs):
    assert user.User().get_user_by_name(inputs).status_code == outputs


@pytest.mark.parametrize('inputs, outputs', [
    ('qwdqwd', 500),
    ('2efed', 500),
    ('erthge45', 500),
])
def test_get_user_by_name_negative(inputs, outputs):
    assert user.User().get_user_by_name(inputs).status_code == outputs
