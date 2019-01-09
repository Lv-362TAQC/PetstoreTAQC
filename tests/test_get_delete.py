""" GET. Find purchase order by ID. For valid response try integer IDs with
    value >= 1 and <= 10. Other values will generated exceptions.
    DELETE. Delete purchase order by ID.For valid response
    try integer IDs with positive integer value.
    Negative or non-integer values will generate API errors. """

import pytest
from store_get_delete import Store


S = Store()


@pytest.mark.parametrize('order_id, output', [(-5, 404), (0, 404), (1, 200),
                                              (2, 200), (3, 200), (4, 200), (5, 200),
                                              (6, 200), (7, 200), (8, 200), (9, 200),
                                              (10, 200), (11, 404), (20, 404)])
def test_get(order_id, output):
    """checking store_get func"""
    assert S.storeget(order_id).status_code == output


@pytest.mark.parametrize('del_id, output', [(17, 404),
                                            (22, 404)])
def test_del(del_id, output):
    """checking store_delete func"""
    assert S.storedelete(del_id).status_code == output
