"""Get a country, Get a city,
Get a name organization, Get a currency
For IP API.
"""

from http import HTTPStatus
import requests
from models.settings import LOGGER


BASE_URL = 'https://ipapi.co/'


class IpApi:
    """Class IpApi"""
    url = BASE_URL

    def __init__(self):
        pass

    def get_country(self, data: str):
        """Get a country"""
        response = requests.get(f"{self.url}{data}/country_name")
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Getting country. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Getting country. Status code: {status}. Something went wrong')
        return response

    def get_city(self, data: str):
        """Get a city"""
        response = requests.get(f"{self.url}{data}/city")
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Getting city. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Getting city. Status code: {status}. Something went wrong')
        return response

    def get_organizations(self, data: str):
        """Get a name organization"""
        response = requests.get(f"{self.url}{data}/org")
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Getting organizations. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Getting organizations. Status code: {status}. Something went wrong')
        return response

    def get_currency(self, data: str):
        """Get a currency"""
        response = requests.get(f"{self.url}{data}/currency")
        status = response.status_code
        if status == HTTPStatus.OK:
            LOGGER.info(f'Getting currency. Status code: {status}. Successful operation.')
            return response
        LOGGER.debug(f'Getting currency. Status code: {status}. Something went wrong')
        return response



