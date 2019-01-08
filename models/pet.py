"""methods for PET object """

from http import HTTPStatus
import json
import logging
import os.path
import requests

""" Configure logger """
LOGGER = logging.getLogger('pet_logs')
LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(filename)-8s %(funcName)-10s '
                              '[LINE:%(lineno)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
if not os.path.exists("../logs/"):
    os.makedirs("../logs/")
file_handler = logging.FileHandler(f'../logs/{LOGGER.name}.log')  # Save log to file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)


class PetModels:
    """
    This is class of methods for Pet category of PetStore

    """

    def __init__(self):
        self.pet_base_url = "https://petstore.swagger.io/v2/pet/"

    def convert_data_to_json(self, data: dict):
        """Method that converts input data to json data"""
        data = str(data).replace("'", "\"")
        json_data = json.loads(data)
        return json_data

    def pet_create_new(self, **create_parameters):
        """
        Method to create new pet in database

        :param **create_parameters - **kwargs values that can be considered:
        - id: int64;
        - category: {
                    id: int64,
                    name: str
                    };
        - name*: str;
        - photoUrls*: [str] #list of strings;
        - tags: [{
                    id: int64,
                    name: str
                    }]; #list of dicts
        - status: str # values that can be used: 'available', 'pending', 'sold'
        Note: * - required parameters

        :return json data
        """
        LOGGER.debug('Convert input data to JSON data')
        json_data = self.convert_data_to_json(create_parameters)
        LOGGER.info(f'input data converted to JSON data: {json_data}')
        LOGGER.debug(f'Request: POST {json_data} to {self.pet_base_url}')
        response_pet_create_new = requests.post(self.pet_base_url, json=json_data)
        if response_pet_create_new.status_code == HTTPStatus.OK:
            LOGGER.info(f'Response: Status code {response_pet_create_new.status_code}' +
                        f'{response_pet_create_new.text}')
        else:
            LOGGER.warning(f'Response: Status code {response_pet_create_new.status_code}' +
                           f'{response_pet_create_new.url} {response_pet_create_new.text}')
        return response_pet_create_new.json()

    def pet_find_by_status(self, status: str):
        """
        Method that finds pet by it`s status in system
        :param status: str values that can be considered:
         - "available"
         - "pending"
         - "sold"
         :return json data
         """
        request_url = self.pet_base_url + "findByStatus?status=" + status
        LOGGER.debug(f'Request: GET {request_url}')
        response_pet_find_by_status = requests.get(request_url)
        if response_pet_find_by_status.status_code == HTTPStatus.OK:
            LOGGER.info(f'Response: Status code { response_pet_find_by_status.status_code}' +
                        f'{ response_pet_find_by_status.text}')
        else:
            LOGGER.warning(f'Response: Status code { response_pet_find_by_status.status_code}' +
                           f'{ response_pet_find_by_status.url} { response_pet_find_by_status.text}')
        return response_pet_find_by_status.json()
