import logging
import logging.config
import os.path
import requests
from http import HTTPStatus

""" Configure logger """
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-15s %(funcName)-20s '
                              '[LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
file_handler = logging.FileHandler(f'../logs/{LOGGER.name}.log')  # Save log to file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)

BASE_URL_STORE = 'http://petstore.swagger.io/v2'


class User:
    def __init__(self):
        self.url = BASE_URL_STORE + '/user'

    def get_user_by_name(self, username: str) -> requests.models.Response:
        """
        Send GET request to http://petstore.swagger.io/v2/<username> and receive JSON with user
        data in it.
        """
        self.url += f'/{username}'
        LOGGER.debug(f'Request: GET {self.url}')
        response = requests.get(f'{self.url}')
        if response.status_code == HTTPStatus.OK:
            LOGGER.info(f'Response: Status code {response.status_code}, {response.text}')
        else:
            LOGGER.warning(f'Response: Status code {response.status_code}, {response.url} '
                           f'{response.text}')
        return response
