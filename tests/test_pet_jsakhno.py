"""Testing pet_find_update_delete"""

import pytest
import json
from models.pet_find_update_delete import Pet

DATA = """{
  "name": "doggo",
  "photoUrls": ["string"],
  "status": "available"
}"""

DATA_JSON = json.loads(DATA)

p = Pet(DATA_JSON)


def test_crating():
    assert p.creat_new_p(DATA_JSON).status_code == 200
    assert p.creat_new_p(DATA_JSON).headers['Content-Type'] == 'application/json'
    assert p.new_pet['name'] == DATA_JSON['name']
    assert p.new_pet['status'] == DATA_JSON['status']


def test_finding():
    assert p.find_b_id(p.pet_id)['name'] == 'doggo'
    assert p.find_b_id('1')['name'] == 'sed'
    assert p.find_b_id('2')['name'] == 'amx'
    assert p.find_b_id('3')['name'] == 'doggie'


def test_all_of_find():
    assert p.new_pet['id'] == p.find_pet['id']
    assert p.new_pet['name'] == p.find_pet['name']
    assert p.new_pet['status'] == p.find_pet['status']


def test_updating():
    new_data = {'name': 'doggo130', 'status': 'sold'}
    p.update_p(p.pet_id, new_data)
    assert p.find_b_id(p.pet_id)['name'] == new_data['name']
    assert p.find_b_id(p.pet_id)['status'] == new_data['status']


def test_deleting():
    p.delete_pet(p.pet_id)
    assert p.find_b_id(p.pet_id)["message"] == "Pet not found"

