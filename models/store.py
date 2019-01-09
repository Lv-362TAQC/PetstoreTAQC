import requests
import json
from models.settings import LOGGER, BASE_URL


class Store:
    url = BASE_URL

    def get_inventory(self):
        response = requests.get(self.url + '/inventory')
        status_code = response.status_code
        LOGGER.info(f'Status code: {status_code}. Successful operation.')
        return response

    def order(self, data: (str, bytes, bytearray)):
        """ Place an order.
        Args:
             data: str - json compatible string
        """
        LOGGER.info("Converting input to JSON format...")
        data_json = json.loads(data)
        LOGGER.info("... input converted.")
        response = requests.post(f"{self.url}/order", json=data_json)
        LOGGER.info(f"POSTed input to address {self.url}/order")
        return response

    def check_order(self, order_id: int):
        """ Check order using it's id. """
        response = requests.get(f"{self.url}/order/{order_id}")
        LOGGER.info(f"Sent GET request for order with id: {order_id}")
        return response

    def del_order(self, order_id: int):
        """ Delete order using it's id. """
        response = requests.delete(f"{self.url}/order/{order_id}")
        LOGGER.info(f"Deleted order with id: {order_id}")
        return response
