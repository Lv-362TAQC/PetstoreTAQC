"""Methods: Lookup a postcode, Bulk lookup postcodes, Get a random postcode.
   For PostCodes API.
"""

import json
from http import HTTPStatus
import requests
from models.settings import LOGGER

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
        """Lookup a postcode."""
        response = requests.get(self.url + "/postcodes/" + post_code)
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Lookup a postcode. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Lookup a postcode. Status code: {status}. Something went wrong')
        return response

    def bulk_lookup(self, data: dict):
        """Bulk lookup postcodes."""
        data_json = json.loads(data)
        response = requests.post(self.url + "/postcodes", json=data_json)
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Bulk lookup postcodes. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Bulk lookup postcodes. Status code: {status}. Something went wrong')
        return response
