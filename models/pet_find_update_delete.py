import requests
import json

BASE_URL = "https://petstore.swagger.io/v2"


class Pet:
    def __init__(self):
        self.url = BASE_URL + "/pet"

    def creat_new_p(self, data_json):
        creat_new_pet = requests.post(self.url, json=data_json)
        self.crnp = creat_new_pet.json()
        return self.crnp

    def pet_id(self):
        self.PET_ID = str(self.crnp['id'])
        return self.PET_ID

    def find_b_id(self):
        find_by_id = requests.get(self.url + "/" + self.PET_ID)
        return find_by_id.json()

    def update_p(self, newname):
        update_pet = requests.post(self.url + "/" + self.PET_ID, data=newname)
        return update_pet

    def delete_pet(self):
        self.delete_pet_by_id = requests.delete(self.url + "/" + self.PET_ID)
        return self.delete_pet_by_id


if __name__ == "__main__":
    pet = Pet()

    data = """{
      "name": "doggo",
      "photoUrls": ["string"],
      "status": "available"
    }"""

    data_json = json.loads(data)

    print(pet.creat_new_p(data_json))
    print(pet.pet_id())
    print(json.dumps(pet.find_b_id(), indent=4))
    newname = {'name': 'doggo130', 'status': 'sold'}
    pet.update_p(newname)
    print(json.dumps(pet.find_b_id(), indent=4))
    pet.delete_pet()
    print('='*126)
    if pet.find_b_id()["message"] == "Pet not found":
        print("\n"*2 + ' '*56 + "Pet deleted!!!" + ' '*56 + "\n"*2)
    else:
        raise ImportError
    print('='*126)
