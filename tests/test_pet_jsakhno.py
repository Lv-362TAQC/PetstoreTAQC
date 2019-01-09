"""Testing pet_find_update_delete"""
from models.pet import Pet, convert_data_to_json
from http import HTTPStatus
import pytest
import json


DATA = {
  "name": "doggo",
  "photoUrls": ["string"],
  "status": "available"
}


p = Pet()
new_pet = p.create_new(name='doggo', photoUrls=["string"], status='available')
json_new_pet = new_pet.json()
pet_id = str(json_new_pet['id'])
def json_re(resp):
    return p.find_by_id(resp).json()

@pytest.mark.parametrize('id, corect_name', [('811563', 'evmicrdsir'),('3663833108', 'hello kity'),('740639', 'Savvy')])
def test_finding(id, corect_name):
    assert json_re(id)['name'] == corect_name


def test_all_of_find():
    assert json_new_pet['id'] == json_re(pet_id)['id']
    assert json_new_pet['name'] == json_re(pet_id)['name']
    assert json_new_pet['status'] == json_re(pet_id)['status']

@pytest.mark.parametrize('param', [('name'),('status')])
def test_updating(param):
    new_data = {'name': 'doggo130', 'status': 'sold'}
    p.update(pet_id, new_data)
    assert json_re(pet_id)[param] == new_data[param]



def test_deleting():
    p.delete_pet(pet_id)
    assert json_re(pet_id)["message"] == "Pet not found"

