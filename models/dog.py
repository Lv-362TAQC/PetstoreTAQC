import json
import logging
import os.path
import requests

BASE_DOG_URL = 'https://dog.ceo/api/'
""" Configure logger """
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-15s %(funcName)-20s [LINE:%(lineno)s] '
                              '%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
file_handler = logging.FileHandler(f'../logs/{logger.name}.log')  # Save log to file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Dog:
    def __init__(self):
        self.url = BASE_DOG_URL

    def get_breed_list(self):
        self.url += 'breeds/list/all'
        logger.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            logger.info(f'Response: Status code {response.status_code}')
        else:
            logger.debug(f'Response: Status code {response.status_code}, {response.text}')
        return response

    def get_random_image(self):
        self.url += 'breeds/image/random'
        logger.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            logger.info(f'Response: Status code: {response.status_code}')
        else:
            logger.debug(f'Response: Status code {response.status_code}, Something bad happened')
        return response

    def get_images_by_breed(self, breed: str):
        self.url += f'breed/{breed}/images'
        logger.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            logger.info(f'Response: Status code: {response.status_code}')
        else:
            logger.debug(f'Response: Status code {response.status_code}, {response.text}, {response.url}')
        return response

    def get_subbreed_by_breed(self, breed: str):
        self.url += f'breed/{breed}/list'
        logger.debug(f'Request: GET {self.url}')
        response = requests.get(self.url)
        if response.status_code == 200:
            logger.info(f'Response: Status code: {response.status_code}')
        else:
            logger.debug(f'Response: Status code {response.status_code}, {response.text}, {response.url}')
        return response
