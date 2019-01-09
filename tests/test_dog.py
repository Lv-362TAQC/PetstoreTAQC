import pytest
import json
from models.dog import Dog
from http import HTTPStatus
import allure

def test_find_request_positive():
    assert Dog._find_request('https://dog.ceo/api/breeds/list/all').status_code == HTTPStatus.OK

def test_find_request_negative():
    assert Dog._find_request('https://dog.ceo/api/wrong/link/all').status_code == HTTPStatus.NOT_FOUND

def test_response_positive():
    assert isinstance(Dog._response('https://dog.ceo/api/breeds/list/all'), dict)

def test_get_random_image():
    assert Dog().get_random_image('https://dog.ceo/api/breeds/image/random')