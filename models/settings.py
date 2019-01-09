from http import HTTPStatus
import logging
import os.path
import json
import requests

LOGGER = logging.getLogger('pet_logs')
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-8s %(funcName)-10s '
                              '[LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
FILE_HANDLER = logging.FileHandler(f'../logs/{LOGGER.name}.log')  # Save log to file
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)


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
