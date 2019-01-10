"""Tests for User model PetStoreAPI."""

import json
import requests
from models.settings import LOGGER, BASE_USER_URL
from http import HTTPStatus



class User:
    """User model."""
    url = BASE_USER_URL

    def __init__(self):
        self.id = None
        self.username = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None
        self.phone = None
        self.user_status = None

    @classmethod
    def _find_user_by_name(cls, username: str) -> requests.models.Response:
        """Send GET request to find user by username."""
        LOGGER.debug(f'Send GET {cls.url}/{username}')
        response = requests.get(f'{cls.url}/{username}')
        LOGGER.info(f'Response: Status code {response.status_code}, '
                    f'{response.text}, '
                    f'{response.url}')
        return response

    def get_user_by_name(self, username: str):
        """Set user's attributes, received from GET request."""
        response = User._find_user_by_name(username)
        LOGGER.info(f'Status code:{response.status_code}, {response.text}')

        if not response.status_code == HTTPStatus.OK:
            LOGGER.warning(f'Status code:{response.status_code}, {response.url}, {response.text}')
            return None

        response = json.loads(response.text)
        self.id = response['id']
        self.username = response['username']
        self.first_name = response['firstName']
        self.last_name = response['lastName']
        self.email = response['email']
        self.password = response['password']
        self.phone = response['phone']
        self.user_status = response['userStatus']

        LOGGER.debug(f'Set user attributes: {self.id}, {self.username}, {self.first_name}, '
                     f'{self.last_name}, {self.email}, {self.password}, {self.phone}, '
                     f'{self.user_status}')
