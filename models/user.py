import logging
import logging.config
import os.path
import requests
import json
from http import HTTPStatus

""" Configure logger """
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-15s %(funcName)-20s '
                              '[LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
file_handler = logging.FileHandler(f'../logs/{LOGGER.name}.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)

BASE_URL_STORE = 'http://petstore.swagger.io/v2'


class User:
    url = BASE_URL_STORE + '/user'

    def __init__(self):
        self.id = None
        self.username = None
        self.firstName = None
        self.lastName = None
        self.email = None
        self.password = None
        self.phone = None
        self.user_status = None

    @classmethod
    def _find_user_by_name(cls, username: str) :
        """
        Returns response from GET request
        :param username: string
        :return: requests.models.Response
        """
        LOGGER.debug(f'Send GET {cls.url}/{username}')
        response = requests.get(f'{cls.url}/{username}')
        LOGGER.info(f'Response: Status code {response.status_code}, {response.text}, {response.url}')
        return response

    def get_user_by_name(self, username: str):
        response = User._find_user_by_name(username)

        if not response.status_code == HTTPStatus.OK:
            LOGGER.debug(f'Status code:{response.status_code}, {response.url}, {response.text}')
            return None

        response = json.loads(response.text)
        self.id = response['id']
        self.username = response['username']
        self.firstName = response['firstName']
        self.lastName = response['lastName']
        self.email = response['email']
        self.password = response['password']
        self.phone = response['phone']
        self.user_status = response['userStatus']
        LOGGER.debug(f'{self.id}, {self.username}, {self.firstName}, {self.lastName}, '
                     f'{self.email}, {self.password}, {self.phone}, {self.user_status}')
