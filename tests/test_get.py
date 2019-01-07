"""GET. Find purchase order by ID. For valid response try integer IDs with
 value >= 1 and <= 10. Other values will generated exceptions"""

import pytest
from store_get import Store

S = Store()


@pytest.mark.parametrize('order_id, get_value', [(-5, 404), (0, 404), ('1', 200),
                                                 ('2', 200), (3, 200), (4, 200), (5, 200),
                                                 (6, 200), (7, 200), (8, 200), (9, 200), (10, 200),
                                                 (11, 404), (20, 404)])
def test_gets(order_id, get_value):
    """checking storeget func"""
    assert S.storeget(order_id).status_code == get_value
