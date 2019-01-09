import logging
import os.path

LOGGER = logging.getLogger('logs')
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-8s %(funcName)-10s '
                              '[LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
FILE_HANDLER = logging.FileHandler(f'../logs/{LOGGER.name}.log')  # Save log to file
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)

# CONSTANTS
BASE_URL = 'https://petstore.swagger.io/v2/store'

# Test data: Store
STORE_TEST_DATA = [
        """{"id": 8, "petId": 0, "quantity": 0, "shipDate": "2019-01-03T20:13:27.011Z",
         "status": "placed", "complete": false}""",
        """{"id": 5, "petId": 5, "quantity": 5, "shipDate": "", "status": "approved",
         "complete": false}""",
        """{"id": 0, "petId": 0, "quantity": 0, "shipDate": "2019-01-09T19:06:26.244Z",
          "status": "placed", "complete": false}"""]
STORE_EMPTY_DATA = """{}"""
STORE_DEFAULT = """{"id":0,"petId":0,"quantity":0,"complete":false}"""
