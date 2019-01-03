import pytest
import json
from models import dog

OK = 200
NOT_FOUND = 404


def test_get_breed_list():
    assert dog.Dog().get_breed_list().status_code == OK


def test_get_random_image():
    assert dog.Dog().get_random_image().status_code == OK


def test_get_random_image_is_jpg():
    assert dog.Dog().get_random_image().text[:-2].endswith('.jpg')


@pytest.mark.parametrize('inputs', ['affenpinscher', 'wolfhound', 'mastiff'])
def test_get_images_by_breed_pos(inputs):
    assert dog.Dog().get_images_by_breed(inputs).status_code == OK


@pytest.mark.parametrize('inputs', ['yorkshire', '234rfcwef2'])
def test_get_images_by_breed_neg(inputs):
    assert dog.Dog().get_images_by_breed(inputs).status_code == NOT_FOUND


def test_get_subbreed_by_breed():
    assert dog.Dog().get_subbreed_by_breed('husky').status_code == OK


@pytest.mark.parametrize('inputs, outputs', [('affenpinscher', []), ('wolfhound', ['irish']), ('mastiff',
                                                                                               ['bull', 'tibetan'])])
def test_get_subbreed_by_breed_pos(inputs, outputs):
    subbreeds = json.loads(dog.Dog().get_subbreed_by_breed(inputs).text)
    assert subbreeds['message'] == outputs

# husky
# @pytest.mark.parametrize('inputs', ['yorkshire', '234rfcwef2'])
# def test_get_images_by_breed_neg(inputs):
#     assert dog.Dog().get_images_by_breed(inputs).status_code == NOT_FOUND

test_get_subbreed_by_breed_pos('mastiff', ['bull', 'tibetan'])