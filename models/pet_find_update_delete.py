import requests
import json

BASE_URL = "https://petstore.swagger.io/v2"


class Pet:
    def __init__(self):
        self.url = BASE_URL + "/pet"

    def cr_n_p(self, data_json):
        creat_new_pet = requests.post(self.url, json=data_json)
        self.crnp = creat_new_pet.json()
        return self.crnp

    def pet_id(self):
        self.PET_ID = str(self.crnp['id'])
        return self.PET_ID

    def fbid(self):
        find_by_id = requests.get(self.url + "/" + self.PET_ID)
        return find_by_id.json()

    def chnp(self, newname):
        chenge_name_pet = requests.post(self.url + "/" + self.PET_ID, data=newname)
        return chenge_name_pet

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

    print(pet.cr_n_p(data_json))
    print(pet.pet_id())
    print(json.dumps(pet.fbid(), indent=4))
    newname = {'name': 'doggo130', 'status': 'sold'}
    pet.chnp(newname)
    print(json.dumps(pet.fbid(), indent=4))
    pet.delete_pet()
    print('='*126)
    if pet.fbid()["message"] == "Pet not found":
        print("\n"*2 + ' '*56 + "Pet deleted!!!" + ' '*56 + "\n"*2)
    else:
        raise ImportError
    print('='*126)
