"""Foreign exchange rates API with currency conversion"""

import requests
from models.settings import LOGGER as logger

BASE_URL = 'https://api.exchangeratesapi.io'


class Latest:
    """Class Latest"""
    url = BASE_URL + '/latest'
    def __init__(self):
        pass


    def latest_foreign(self):
        """Get the latest foreign exchange reference rates"""
        response = requests.get(self.url)
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url}")
        return response


    def latest_base(self):
        """Rates are quoted against the Euro by default.
        Quote against a different currency by setting the base parameter in your request
        """
        response = requests.get(self.url + '?base=USD')
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url + '?base=USD'}")
        return response


    def latest_symbols(self):
        """Request specific exchange rates by setting the symbols parameter"""
        response = requests.get(self.url + '?symbols=USD,GBP')
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url + '?symbols=USD,GBP'}")
        return response


class Day:
    """Class Day"""
    url = BASE_URL + '/2010-01-12'
    def __init__(self):
        pass


    def historical(self):
        """Get historical rates for any day since 1999"""
        response = requests.get(self.url)
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url}")
        return response


class History:
    """Class History"""
    url = BASE_URL + '/history'
    def __init__(self):
        pass


    def rates_time_period(self):
        """Get historical rates for a time period"""
        response = requests.get(self.url + '?start_at=2018-01-01&end_at=2018-09-01')
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01'}")
        return response


    def specific_exchange_rates(self):
        """Limit results to specific exchange rates to save bandwidth with the symbols parameter"""
        response = requests.get(self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY')
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY'}")
        return response


    def different_currency(self):
        """Quote the historical rates against a different currency"""
        response = requests.get(self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD')
        status_code = response.status_code
        logger.info(f"Code status: {status_code}. Successful operation. "
                    f"URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD'}")
        return response
