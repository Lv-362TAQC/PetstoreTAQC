import pytest
import json
from models.dog_api import Dog
from http import HTTPStatus
import allure

@allure.step
def step_response_ok(response) -> None:
    assert response.status_code == HTTPStatus.OK

@allure.step
def step_response_not_found(response):
    assert response.status_code == HTTPStatus.NOT_FOUND

@allure.step
def step_is_image(response):
    assert response.text[:-2].lower().endswith('.jpg'.lower())
    return response.text[:-2]


@allure.step
def step_expected_response(response, expexted_response):
    response = json.loads(response.text)
    assert response['message'] == expexted_response


@allure.severity(severity_level=allure.severity_level.BLOCKER)
def test_get_breed_list():
    step_response_ok(Dog().get_breed_list())


@allure.severity(severity_level=allure.severity_level.MINOR)
def test_get_random_image():
    response = Dog().get_random_image()
    step_response_ok(response)
    step_is_image(response)


@allure.severity(severity_level=allure.severity_level.CRITICAL)
@pytest.mark.parametrize('inputs', ['affenpinscher', 'wolfhound', 'mastiff'])
def test_get_images_by_breed_pos(inputs):
    response = Dog().get_images_by_breed(inputs)
    step_response_ok(response)


@pytest.mark.parametrize('inputs', ['yorkshire', '234rfcwef2'])
def test_get_images_by_breed_neg(inputs):
    response = Dog().get_images_by_breed(inputs)
    step_response_not_found(response)


@pytest.mark.parametrize('inputs, outputs', [('affenpinscher', []),
                                             ('wolfhound', ['irish']),
                                             ('mastiff', ['bull', 'tibetan'])])
def test_get_subbreed_by_breed_pos(inputs, outputs):
    response = Dog().get_subbreed_by_breed(inputs)
    step_response_ok(response)
    step_expected_response(response, outputs)
