"""Tests for DodAPI."""

from models.dog import Dog
from http import HTTPStatus
import allure
import pytest
from models.settings import DOD_SUBBREEDS, DOG_LINK_TYPE


@allure.story('DogAPI')
@allure.step('Check if input is image url')
def step_is_jpg_image(url: str):
    assert url.lower().endswith('.jpg')
    allure.attach(url, attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
def test_find_request_positive():
    response = Dog._find_request('https://dog.ceo/api/breeds/list/all')
    with allure.step("Check status code, with valid url"):
        assert response.status_code == HTTPStatus.OK
    allure.attach(response.text, attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
def test_find_request_negative():
    response = Dog._find_request('https://dog.ceo/api/wrong/link/all')
    with allure.step("Check status code, with invalid url"):
        assert response.status_code == HTTPStatus.NOT_FOUND
    allure.attach(response.text, attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
@pytest.mark.parametrize(('inputs', 'outputs'), DOG_LINK_TYPE)
def test_response_type_message(inputs, outputs):
    response = Dog._response(inputs)
    with allure.step("Check output type"):
        assert isinstance(response, outputs)
    allure.attach(str(response), attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
def test_get_breed_list():
    dogs_list = Dog().get_breed_list()
    with allure.step('Check if \'husky\' breed in output dict'):
        assert 'husky' in dogs_list
    with allure.step('Check if \'meow\' breed not in output dict'):
        assert 'meow' not in dogs_list
    allure.attach(str(dogs_list), attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
def test_get_random_image():
    step_is_jpg_image(Dog().get_random_image())


@allure.step
@allure.story('DogAPI')
def test_get_images_by_breed():
    response_text = Dog().get_images_by_breed('hound')
    for item in response_text:
        step_is_jpg_image(item)
    allure.attach(str(response_text), attachment_type=allure.attachment_type.TEXT)


@allure.step
@allure.story('DogAPI')
@pytest.mark.parametrize('inputs, outputs', DOD_SUBBREEDS)
def test_get_subbreed_by_breed(inputs, outputs):
    subbreed = Dog().get_subbreed_by_breed(inputs)
    assert subbreed == outputs


@allure.step
@allure.story('DogAPI')
def test_get_breed_random_image():
    step_is_jpg_image(Dog().get_breed_random_image('husky'))
