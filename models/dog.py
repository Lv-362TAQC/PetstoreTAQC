"""."""
import json
import logging
import logging.config
import os.path
import requests
from http import HTTPStatus

BASE_DOG_URL = 'https://dog.ceo/api/'

""" Configure logger """
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-15s %(funcName)-20s ['
                              'LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
file_handler = logging.FileHandler(f'../logs/{LOGGER.name}.log')  # Save log to file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
LOGGER.addHandler(file_handler)


class Dog:
    url = BASE_DOG_URL

    def __init__(self):
        self.breeds_list = None
        self.random_image = None
        self.breeds_image = None
        self.subbreeds = None

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
        print(json.loads(response.text)['message'])
        return json.loads(response.text)['message']

    def get_breed_list(self) -> dict or None:
        self.breeds_list = Dog._response(self.url + 'breeds/list/all')
        return self.breeds_list

    def get_random_image(self) -> str or None:
        self.breeds_list = Dog._response(self.url + 'breeds/image/random')
        return self.get_random_image()

    def get_images_by_breed(self, breed: str) -> list:
        """
        Send GET request to https://dog.ceo/api/breed/<breed name>/images/image/random and receive
        JSON with list of URLs in it.
        """
        self.breeds_list = Dog._response(self.url + f'breed/{breed}/images')
        return self.breeds_image

    def get_subbreed_by_breed(self, breed: str) -> list:
        """
        Send GET request to https://dog.ceo/api/beed/<breed name>/list and receive JSON with list
        of subbreeds in it.
        """
        self.subbreeds = Dog._response(self.url + f'breed/{breed}/list')
        return  self.subbreeds

