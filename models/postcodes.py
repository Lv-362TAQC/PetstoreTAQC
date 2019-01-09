"""Lookup a postcode, Bulk lookup postcodes, Get a random postcode.
   For PostCodes API.
"""

import json
import logging
import os.path
from http import HTTPStatus
import requests


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
if not os.path.exists("logs/"):
    os.makedirs("logs/")
FILE_HANDLER = logging.FileHandler(f'logs/{LOGGER.name}.log')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(FILE_HANDLER)


BASE_URL = 'https://postcodes.io/'


class PostCode:
    """Class Postcodes"""
    url = BASE_URL

    def __init__(self):
        pass

    def random(self):
        """Get a random postcode."""
        response = requests.get(self.url + '/random/postcodes')
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Getting random postcode. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Getting random postcode. Status code: {status}. Something went wrong')
        return response

    def lookup(self, post_code: str):
        """Lookup a postcode"""
        response = requests.get(self.url + "/postcodes/" + post_code)
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Lookup a postcode. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Lookup a postcode. Status code: {status}. Something went wrong')
        return response

    def bulk_lookup(self, data: dict):
        """Bulk lookup postcodes"""
        data_json = json.loads(data)
        response = requests.post(self.url + "/postcodes", json=data_json)
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Bulk lookup postcodes. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Bulk lookup postcodes. Status code: {status}. Something went wrong')
        return response
