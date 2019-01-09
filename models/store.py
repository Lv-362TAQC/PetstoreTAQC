import requests
import json
from models.logger import logger

BASE_URL = 'https://petstore.swagger.io/v2/store'


class Store:
    def __init__(self):
        self.url = BASE_URL

    def get_inventory(self):
        response = requests.get(self.url + '/inventory')
        status_code = response.status_code
        if status_code == 200:
            logger.info(f'Status code: {status_code}. Successful operation.')
            return response     # json.dumps(response.json(), ensure_ascii=False, indent=4)
        else:
            logger.info(f'Status code: {status_code}. Something went wrong')
            return response

    def order(self, data: str):
        """ Place an order.
        Args:
             data: str - json compatible string
        """
        logger.info("Converting input to JSON format...")
        data_json = json.loads(data)
        logger.info("... input converted.")
        try:
            response = requests.post(f"{self.url}/order", json=data_json)
            logger.info(f"POSTed input to address {self.url}/order")
        except TypeError:
            logger.exception(f'Status code: {response.status_code},\n{response}')
        return response

    def check_order(self, order_id: int):
        """ Check order using it's id. """
        response = requests.get(f"{self.url}/order/{order_id}")
        return response.json()

    def del_order(self, order_id: int):
        """ Delete order using it's id. """
        response = requests.delete(f"{self.url}/order/{order_id}")
        return response
