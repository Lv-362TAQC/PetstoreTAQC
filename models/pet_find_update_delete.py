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


BASE_URL = "https://petstore.swagger.io/v2"


class Pet:
    """
    PET
    """
    def __init__(self, data_json: dict):
        """
        constructor
        :param data_json: dict
        """
        self.url = BASE_URL + "/pet"
        self.new_pet = self.creat_new_p(data_json).json()
        self.pet_id = str(self.get_pet_id())
        self.find_pet = self.find_b_id(self.pet_id)

    def creat_new_p(self, data_json: dict):
        """
        create new pet(need json file)
        :param data_json: dict
        :return:
        """
        resp = requests.post(self.url, json=data_json)
        code = resp.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'CREATING...Status code: {code}. Successful operation.')
            return resp
        LOGGER.warning(f'CREATING...Status code: {code}. Something went wrong')
        return resp

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
        resp = requests.post(self.url + "/" + pet_id, data=new_name)
        code = resp.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'UPDATING...Status code: {code}. Successful operation.')
            return resp
        LOGGER.warning(f'UPDATING...Status code: {code}. Something went wrong')
        return resp

    def delete_pet(self, pet_id: str):
        """
        deleting pet from store
        :param pet_id: str
        :return:
        """
        resp = requests.delete(self.url + "/" + pet_id)
        code = resp.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'DELETING...Status code: {code}. Successful operation.')
            return resp
        LOGGER.warning(f'DELETING...Status code: {code}. Something went wrong')
        return resp


if __name__ == "__main__":

    DATA = """{
      "name": "doggo",
      "photoUrls": ["string"],
      "status": "available"
    }"""

    DATA_JSON = json.loads(DATA)
    NEW_NAME = {'name': 'doggo130', 'status': 'sold'}
    PET = Pet(DATA_JSON)

    print(PET.new_pet)
    print(PET.pet_id)
    print(json.dumps(PET.find_b_id(PET.pet_id), indent=4))
    PET.update_p(PET.pet_id, NEW_NAME)
    print(json.dumps(PET.find_b_id(PET.pet_id), indent=4))
    PET.delete_pet(PET.pet_id)
    print('='*126)
    if PET.find_b_id(PET.pet_id)["message"] == "Pet not found":
        print("\n"*2 + ' '*56 + "Pet deleted!!!" + ' '*56 + "\n"*2)
    else:
        raise ImportError
    print('='*126)
