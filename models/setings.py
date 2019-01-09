from http import HTTPStatus
import logging
import os.path
import json
import requests


class LogginSettings:
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)
        self.LOGGER.setLevel(logging.DEBUG)

        self.FORMATTER = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                                      datefmt='%d/%m/%Y %H:%M:%S')
        if not os.path.exists("logs/"):
            os.makedirs("logs/")
        self.FILE_HANDLER = logging.FileHandler(f'logs/{self.LOGGER.name}.log')
        self.FILE_HANDLER.setLevel(logging.DEBUG)
        self.FILE_HANDLER.setFormatter(self.FORMATTER)
        self.LOGGER.addHandler(self.FILE_HANDLER)

    def loggin(self, response):
        code = response.status_code
        if code == HTTPStatus.OK:
            self.LOGGER.info(f'CREATING...Status code: {code}. Successful operation.')
            return response
        self.LOGGER.warning(f'CREATING...Status code: {code}. Something went wrong')
        return response


if __name__ == "__main__":
    DATA = """{
          "name": "doggo",
          "photoUrls": ["string"],
          "status": "available"
        }"""
    BASE_URL = "https://petstore.swagger.io/v2/pet"
    DATA_JSON = json.loads(DATA)
    NEW_NAME = {'name': 'doggo130', 'status': 'sold'}
    ls = LogginSettings()
    response = requests.post(BASE_URL, json=DATA_JSON)
    serf =ls.loggin(response).json()
    print(serf)
