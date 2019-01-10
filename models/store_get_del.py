"""GET. Find purchase order by ID. For valid response try integer IDs with
 value >= 1 and <= 10. Other values will generated exceptions.
 DELETE  Delete purchase order by ID.For valid response
 try integer IDs with positive integer value.
 Negative or non-integer values will generate API errors """

import logging
import requests
from settings import BASE_URL_ORD


LOGGER = logging.getLogger()

logging.basicConfig(filename="api.log",
                    level=logging.INFO,
                    format="%(levelname)s %(asctime)s - %(message)s",
                    filemode='w')


class Store:
    """Creating class for testing GET & DELETE methods."""
    def __init__(self):
        self.url = BASE_URL_ORD

    def storeget(self, order_id):
        """Sending request with order id"""
        response = requests.get(self.url + str(order_id))
        LOGGER.info("{} {} {}".format(response, order_id, response.json()))
        return response

    def storedelete(self, del_id):
        """DELETE data"""
        response = requests.delete(self.url + str(del_id))
        return response
