"""Tests for POST /pet (add a new pet) and GET /pet/findByStatus (find by status"""
from http import HTTPStatus
from models.pet import Pet, convert_data_to_json
import pytest
import allure
import json


@pytest.mark.parametrize('input, output',
                         [
                          # add one valid parameter to request when two are required
                          ({'name': 'hyfugviust'}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'id': 100}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'photoUrls': ['Url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 765, 'name': 'new_category'}}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': {'id': 1, 'name': 'new_tag'}}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'status': 'pending'}, HTTPStatus.METHOD_NOT_ALLOWED),
                          # add two required parameters with invalid data)
                          ({'name': 786, 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'name': '', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'name': 'some name', 'photoUrls': [2343,1234,435]}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'name': 'some name', 'photoUrls': ''}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'name': 'some name', 'photoUrls': ['']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          # add two required parameters with valid value and id with invalid data
                          ({'id': '123', 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'id': 123.456, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'id': -9223372036854775809, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'id': 9223372036854775809, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          # add two required parameters with valid value and category with invalid data
                          ({'category': 'foo', 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': 10, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 'foo', 'name': 'new_category'},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': -9223372036854775809, 'name': 'new_category'},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 9223372036854775809, 'name': 'new_category'},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 922.566, 'name': 'new_category'},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': '', 'name': 'new_category'},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 777, 'name': 777},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'category': {'id': 777, 'name': ''},
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          # add two required parameters with valid value and tags with invalid data
                          ({'tags': 'foo', 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': 10, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': 'foo', 'name': 'new_tags'}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': -9223372036854775809, 'name': 'new_tags'}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': 9223372036854775809, 'name': 'new_tags'}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': 922.566, 'name': 'new_tags'}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': '', 'name': 'new_tags'}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': 777, 'name': 777}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'tags': [{'id': 777, 'name': ''}],
                            'name': 'some name', 'photoUrls': ['some_url']}, HTTPStatus.METHOD_NOT_ALLOWED),
                          # add two required parameters with valid value and tags with invalid data
                          ({'status': '', 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'status': 'smthg', 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ({'status': 12, 'name': 'some name', 'photoUrls': ['some_url']},
                           HTTPStatus.METHOD_NOT_ALLOWED),
                          ]
                         )
def test_add_pet_negative(input, output):
    assert Pet().create_new(**input).status_code == output


@pytest.mark.parametrize('input, output',
                         [({'name': '786', 'photoUrls': ['some_url1', 'some_url2']}, HTTPStatus.OK),
                          ({'id': 1092, 'name': '786', 'photoUrls': ['some_url1'],
                            'category': {'id': 43754, 'name': 'foo'}, 'tags': [{'id': 9876534, 'name': 'foo'}],
                            'status': 'pending'}, HTTPStatus.OK)
                          ])
def test_add_pet_positive(input, output):
    assert Pet().create_new(**input).status_code == output
    if 'id' in input:
        assert Pet().create_new(**input).json()['id'] == input['id']


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_find_by_status(status):
    var = Pet().find_by_status(status).json()
    print(var)
    for record in var:
        assert record['status'] == status

####################################################################################################################

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
@pytest.mark.parametrize('param', [('id'),
                                   ('name'),
                                   ('status')])
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
