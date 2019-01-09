"""."""
import json
import requests
from http import HTTPStatus
from models.settings import LOGGER, BASE_DOG_URL



class Dog:
    url = BASE_DOG_URL

    def __init__(self):
        self.breeds_list = None
        self.random_image = None
        self.breeds_image = None
        self.subbreeds = None
        self.breed_random_image = None

    @classmethod
    def _find_request(cls, url:str) -> requests.models.Response:
        LOGGER.debug(f'Request: GET {url}')
        response = requests.get(url)
        LOGGER.info(f'Response: Status code {response.status_code}, {response.text}, {response.url}')
        return response

    @classmethod
    def _response(cls, url):
        response = Dog._find_request(url)

        if not response.status_code == HTTPStatus.OK:
            return None
        return json.loads(response.text)['message']

    def get_breed_list(self) -> dict:
        self.breeds_list = Dog._response(self.url + 'breeds/list/all')
        return self.breeds_list

    def get_random_image(self) -> str:
        self.random_image = Dog._response(self.url + 'breeds/image/random')
        return self.random_image

    def get_images_by_breed(self, breed: str) -> list:
        """
        Send GET request to https://dog.ceo/api/breed/<breed name>/images/image/random and receive
        JSON with list of URLs in it.
        """
        self.breeds_list = Dog._response(self.url + f'breed/{breed}/images')
        return self.breeds_list

    def get_subbreed_by_breed(self, breed: str) -> list:
        """
        Send GET request to https://dog.ceo/api/beed/<breed name>/list and receive JSON with list
        of subbreeds in it.
        """
        self.subbreeds = Dog._response(self.url + f'breed/{breed}/list')
        return  self.subbreeds

    def get_breed_random_image(self, breed: str):
        self.breed_random_image = Dog._response(self.url + f'breed/{breed}/images/random')
        return self.breed_random_image
