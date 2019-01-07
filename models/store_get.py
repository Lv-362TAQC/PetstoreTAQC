"""GET. Find purchase order by ID. For valid response try integer IDs with
 value >= 1 and <= 10. Other values will generated exceptions """

# import json
import logging
import requests
BASE_URL = "https://petstore.swagger.io/v2"


LOGGER = logging.getLogger()

logging.basicConfig(filename="D://api.log",
                    level=logging.INFO,
                    format="%(levelname)s - %(message)s",
                    filemode='w')


class Store:
    """Creating class for GET method."""
    def __init__(self):
        self.url = BASE_URL

    def storeget(self, order_id):
        """Sending request with order id"""
        response = requests.get(BASE_URL + "/store/order/" + str(order_id))
        status = response.status_code
        if status == 200:
            LOGGER.info("{}".format(response))
            LOGGER.warning("{}".format(response.json()))
        else:
            LOGGER.info("{} - {}".format(response, 'Wrong ID value. Sorry'))
        return response


# h = Store()
# h.storeget(0)
