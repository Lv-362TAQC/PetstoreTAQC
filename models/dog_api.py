"""."""
import json
import logging
import logging.config
import os.path
import requests

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
    def __init__(self):
        self.url = BASE_DOG_URL

    def get_breed_list(self) -> requests.models.Response:
        """
        Send GET request to https://dog.ceo/api/breeds/list/all and receive JSON with breeds.
        """
        self.url += 'breeds/list/all'
        LOGGER.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            LOGGER.info(f'Response: Status code {response.status_code}')
        else:
            LOGGER.debug(f'Response: Status code {response.status_code}, {response.text}')
        print(type(response))
        return response

    def get_random_image(self):
        """
        Send GET request to https://dog.ceo/api/breeds/image/random and receive JSON with URL in it.
        """
        self.url += 'breeds/image/random'
        LOGGER.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            LOGGER.info(f'Response: Status code: {response.status_code}')
        else:
            LOGGER.debug(f'Response: Status code {response.status_code}, {response.text}, '
                         f'{response.url}')
        return response

    def get_images_by_breed(self, breed: str):
        """
        Send GET request to https://dog.ceo/api/breed/<breed name>/images/image/random and receive
        JSON with list of URLs in it.
        """
        self.url += f'breed/{breed}/images'
        LOGGER.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            LOGGER.info(f'Response: Status code: {response.status_code}')
        else:
            LOGGER.debug(f'Response: Status code {response.status_code}, {response.text}, '
                         f'{response.url}')
        return response

    def get_subbreed_by_breed(self, breed: str):
        """
        Send GET request to https://dog.ceo/api/beed/<breed name>/list and receive JSON with list
        of subbreeds in it.
        """
        self.url += f'breed/{breed}/list'
        LOGGER.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            LOGGER.info(f'Response: Status code: {response.status_code}')
        else:
            LOGGER.debug(f'Response: Status code {response.status_code}, {response.text}, '
                         f'{response.url}')
        return response
