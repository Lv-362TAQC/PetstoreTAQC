""" In this module we are trying to create, find by id, update and delete pets in our store """
from modells import Models
import json


class Pet:
    """
    PET
    """

    BASE_URL = "https://petstore.swagger.io/v2"
    model = Models()

    def __init__(self):
        """
        constructor
        """
        self.id = None
        self.category = None
        self.name = None
        self.photo = None
        self.tags = None
        self.status = None

    @classmethod
    def _creat_new(cls, data=None, json=None):
        """
        create new pet(need json file)
        :param data_json: dict
        :return:
        """
        url = cls.BASE_URL + "/pet"
        response = cls.model.post(url, data=data, json=json)
        return response

    def get_info_new(self,  data_json):
        response = Pet.creat_new(data_json)
        response = json.loads(response.text)
        self.id = response['id']
        self.category = response['category']
        self.name = response['name']
        self.photo = response['photoUrls']
        self.tags = response['tags']
        self.status = response['status']
        return self

    @classmethod
    def _find_by_id(cls, pet_id: str):
        """
        finding pet by id
        :param pet_id: str
        :return:
        """
        url = cls.url + "/" + pet_id
        response = cls.model.get(url)
        return response

    def get_info_fined(self, pet_id):
        response = Pet._find_by_id(pet_id)
        response = json.loads(response.text)
        self.id = response['id']
        self.category = response['category']
        self.name = response['name']
        self.photo = response['photoUrls']
        self.tags = response['tags']
        self.status = response['status']
        return self

    @classmethod
    def _update(cls, pet_id: str, new_data: dict):
        """
        updating pets info
        :param pet_id: str
        :param new_name: dict
        :return:
        """
        url = cls.url + '/' + pet_id
        response = cls.model.post(url, data=new_data)
        return response

    def get_updated_info(self, pet_id, new_data):
        response = Pet._update(pet_id, new_data).text
        self.id = response['id']
        self.category = response['category']
        self.name = response['name']
        self.photo = response['photoUrls']
        self.tags = response['tags']
        self.status = response['status']
        return self

    @classmethod
    def _delete(cls, pet_id: str):
        """
        deleting pet from store
        :param pet_id: str
        :return:
        """
        url = cls.url + "/" + pet_id
        response = cls.model.delete(url)
        return response

    def delete_go(self, pet_id):
        response = Pet._delete(pet_id)
        return response
