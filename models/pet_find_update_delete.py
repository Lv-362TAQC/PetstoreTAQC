""" In this module we are trying to create, find by id, update and delete pets in our store """
from http import HTTPStatus
import json
import logging
import os.path
import requests

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
if not os.path.exists("logs/"):
    os.makedirs("logs/")
FILE_HANDLER = logging.FileHandler(f'logs/{LOGGER.name}.log')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)


class Pet:
    """
    PET
    """

    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self, data_json: dict):
        """
        constructor
        :param data_json: dict
        """
        self.url = self.BASE_URL + "/pet"
        self.id = str(self.get_pet_id())
        self.find_pet = self.find_b_id(self.pet_id)


    def get_pet_id(self):
        """
        get pets id from json file
        :return:
        """
        return self.new_pet['id']

    def find_b_id(self, pet_id: str):
        """
        finding pet by id
        :param pet_id: str
        :return:
        """
        return requests.get(self.url + "/" + pet_id).json()

    def update_p(self, pet_id: str, new_name: dict):
        """
        updating pets info
        :param pet_id: str
        :param new_name: dict
        :return:
        """
        response = requests.post(self.url + "/" + pet_id, data=new_name)
        code = response.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'UPDATING...Status code: {code}. Successful operation.')
            return response
        LOGGER.warning(f'UPDATING...Status code: {code}. Something went wrong')
        return response

    def delete_pet(self, pet_id: str):
        """
        deleting pet from store
        :param pet_id: str
        :return:
        """
        url = self.url + "/" + pet_id
        response = requests.delete(url)
        code = response.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'DELETING...Status code: {code}. Successful operation.')
            return response
        LOGGER.warning(f'DELETING...Status code: {code}. Something went wrong')
        return response
