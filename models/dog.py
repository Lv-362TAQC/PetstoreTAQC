"""."""
import json
import requests
from http import HTTPStatus
from models.settings import LOGGER, BASE_DOG_URL


class Dog:
    """Dog model"""
    url = BASE_DOG_URL

    def __init__(self):
        self.breeds_list = None
        self.random_image = None
        self.breeds_image = None
        self.subbreeds = None
        self.breed_random_image = None

    @classmethod
    def _find_request(cls, url: str) -> requests.models.Response:
        """Send GET request to url.

        :param url: string
        :return: requests.models.Response
        """
        LOGGER.debug(f'Request: GET {url}')
        response = requests.get(url)
        LOGGER.info(f'Response: Status code {response.status_code}')
        return response

    @classmethod
    def _response(cls, url: str):
        """Returns response message"""
        response = Dog._find_request(url)

        if not response.status_code == HTTPStatus.OK:
            LOGGER.warning(f'Response: Status code {response.status_code}, {response.text}, '
                           f'{response.url}')
            return None

        return json.loads(response.text)['message']

    def get_breed_list(self) -> (dict, None):
        """Send GET request to https://dog.ceo/api/breeds/list/all and returns dictionary of breeds
        or None if data weren't received"""
        self.breeds_list = Dog._response(self.url + 'breeds/list/all')
        return self.breeds_list

    def get_random_image(self) -> (str, None):
        """Send GET request to https://dog.ceo/api/breeds/image/random and returns random image url
        or None if data weren't received"""
        self.random_image = Dog._response(self.url + 'breeds/image/random')
        return self.random_image

    def get_images_by_breed(self, breed: str) -> (list, None):
        """Send GET request to https://dog.ceo/api/breed/<breed name>/images/image/random
        and receive list of URLs in it."""
        self.breeds_list = Dog._response(self.url + f'breed/{breed}/images')
        return self.breeds_list

    def get_subbreed_by_breed(self, breed: str) -> (list, None):
        """Send GET request to https://dog.ceo/api/beed/<breed name>/list and receive  list
        of subbreeds in it."""
        self.subbreeds = Dog._response(self.url + f'breed/{breed}/list')
        return self.subbreeds

    def get_breed_random_image(self, breed: str) -> (str, None):
        """Send GET request to https://dog.ceo/api/breed/<breed name>/images/random and
        receive random image url
        of breeds in it."""
        self.breed_random_image = Dog._response(self.url + f'breed/{breed}/images/random')
        return self.breed_random_image
