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
