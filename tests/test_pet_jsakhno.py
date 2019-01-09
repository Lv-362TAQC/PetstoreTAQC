"""Testing pet_find_update_delete"""
from models.pet import Pet, convert_data_to_json
from http import HTTPStatus
import pytest
import json
import allure


DATA = {
  "name": "doggo",
  "photoUrls": ["string"],
  "status": "available"
}


p = Pet()
new_pet = p.create_new(name='doggie', photoUrls=["string"], status='available')
json_new_pet = new_pet.json()
pet_id = str(json_new_pet['id'])


def json_re(resp):
    return p.find_by_id(resp).json()


@allure.step('1')
@pytest.mark.parametrize('id, corect_name', [('811563', 'evmicrdsir'), ('3663833108', 'hello kity'), ('740639', 'Savvy')])
def test_finding(id, corect_name):
    with allure.step('Check finding by id.'):
        assert json_re(id)['name'] == corect_name


@allure.step('2')
@pytest.mark.parametrize('param', [('id'), ('name'), ('status')])
def test_all_of_find(param):
    with allure.step('Check all param finding by id.'):
        assert json_new_pet[param] == json_re(pet_id)[param]


@allure.step('3')
@pytest.mark.parametrize('param', [('name'), ('status')])
def test_updating(param):
    new_data = {'name': 'doggo130', 'status': 'sold'}
    p.update(pet_id, new_data)
    with allure.step('Check updating.'):
        assert json_re(pet_id)[param] == new_data[param]


@allure.step('4')
def test_deleting():
    p.delete_pet(pet_id)
    with allure.step('Check deleting.'):
        assert json_re(pet_id)["message"] == "Pet not found"
