"""Tests for POST /pet (add a new pet) and GET /pet/findByStatus (find by status"""
#from http import HTTPStatus
from models.pet import Pet
import pytest


import allure

@pytest.mark.parametrize('input1, output', [({'name':'hyfugviust', 'photoUrls':[]}, 200)])
def test_add_pet_negative(input1, output):
    """
    test
    """
    print(input1)
    assert Pet().create_new(**input1).status_code == output


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_find_by_status(status):
    var = Pet().find_by_status(status).json()
    print(var)
    for record in var:
        assert record['status'] == status

