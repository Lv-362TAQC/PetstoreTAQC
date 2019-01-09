from setings import LogginSettings
import json
import requests


class Models:
    def __init__(self):
        self.ls = LogginSettings()


    def get(self, url, params=None, **kwargs):
        response = requests.get(url, params=params, **kwargs)
        self.ls.loggin(response)
        return response

    def post(self, url, data=None, json=None):
        response = requests.post(url, data=data, json=json)
        self.ls.loggin(response)
        return response

    def delete(self, url, **kwargs):
        response = requests.delete(url, **kwargs)
        self.ls.loggin(response)
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
    PET = Models()

    print(PET.post(BASE_URL, json=DATA_JSON).json())
    # print(PET.pet_id)
    # print(json.dumps(PET.find_b_id(PET.pet_id), indent=4))
    # PET.update_p(PET.pet_id, NEW_NAME)
    # print(json.dumps(PET.find_b_id(PET.pet_id), indent=4))
    # PET.delete_pet(PET.pet_id)
    # print('='*126)
    # if PET.find_b_id(PET.pet_id)["message"] == "Pet not found":
    #     print("\n"*2 + ' '*56 + "Pet deleted!!!" + ' '*56 + "\n"*2)
    # else:
    #     raise ImportError
    # print('='*126)
