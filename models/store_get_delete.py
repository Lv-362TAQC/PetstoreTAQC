"""GET. Find purchase order by ID. For valid response try integer IDs with
 value >= 1 and <= 10. Other values will generated exceptions.
 DELETE  Delete purchase order by ID.For valid response
 try integer IDs with positive integer value.
 Negative or non-integer values will generate API errors """

import logging
from http import HTTPStatus
import requests

BASE_URL = "https://petstore.swagger.io/v2/store"


LOGGER = logging.getLogger()

logging.basicConfig(filename="api.log",
                    level=logging.INFO,
                    format="%(levelname)s - %(message)s",
                    filemode='w')


class Store:
    """Creating class for testing GET & DELETE methods."""
    def __init__(self):
        self.url = BASE_URL

    def storeget(self, order_id):
        """Sending request with order id"""
        response = requests.get(BASE_URL + '/order/' + str(order_id))
        if response.status_code == HTTPStatus.OK:
            LOGGER.info("{} - {}".format('OK', response.json()))
        else:
            LOGGER.info("{} {} is {}".format(response, order_id, 'wrong ID value. Sorry'))
        return response

    def storedelete(self, del_id):
        """DELETE data"""
        response = requests.delete(BASE_URL + '/order/' + str(del_id))
        return response
