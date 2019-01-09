"""methods for PET object """

from http import HTTPStatus
import json
import requests
from models.settings import LOGGER


def convert_data_to_json(data: dict):
    """Method that converts input data to json data"""
    data = str(data).replace("'", "\"")
    json_data = json.loads(data)
    return json_data


class Pet:
    """
    This is class of methods for Pet category of PetStore

    """

    base_url = "https://petstore.swagger.io/v2/pet/"

    def create_new(self, **create_parameters):
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
        json_data = convert_data_to_json(create_parameters)
        LOGGER.info(f'input data converted to JSON data: {json_data}')
        LOGGER.debug(f'Request: POST {json_data} to {self.base_url}')

        response_create_new = requests.post(self.base_url, json=json_data)
        if response_create_new.status_code == HTTPStatus.OK:
            LOGGER.info(f'Response: Status code {response_create_new.status_code}' +
                        f'{response_create_new.text}')
        else:
            LOGGER.warning(f'Response: Status code {response_create_new.status_code}' +
                           f'{response_create_new.url} {response_create_new.text}')
        return response_create_new

    def find_by_status(self, status: str):
        """
        Method that finds pet by it`s status in system
        :param status: str values that can be considered:
         - "available"
         - "pending"
         - "sold"
         :return json data
         """
        request_url = self.base_url + "findByStatus?status=" + status
        LOGGER.debug(f'Request: GET {request_url}')
        response_find_by_status = requests.get(request_url)
        if response_find_by_status.status_code == HTTPStatus.OK:
            print(response_find_by_status.text)
            LOGGER.info(f'Response: Status code { response_find_by_status.status_code}' +
                        f'{ response_find_by_status.text[:100]}')
        else:
            LOGGER.warning(f'Response: Status code { response_find_by_status.status_code}' +
                           f'{ response_find_by_status.url} { response_find_by_status.text[:100]}')
        return response_find_by_status

    def find_by_id(self, pet_id: str):
        """
        finding pet by id
        :param pet_id: str
        :return:
        """
        response = requests.get(self.base_url + pet_id)
        return response

    def update(self, pet_id: str, new_name: dict):
        """
        updating pets info
        :param pet_id: str
        :param new_name: dict
        :return:
        """
        response = requests.post(self.base_url + pet_id, data=new_name)
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
        url = self.base_url + pet_id
        response = requests.delete(url)
        code = response.status_code
        if code == HTTPStatus.OK:
            LOGGER.info(f'DELETING...Status code: {code}. Successful operation.')
            return response
        LOGGER.warning(f'DELETING...Status code: {code}. Something went wrong')
        return response
