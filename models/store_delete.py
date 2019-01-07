"""For valid response try integer IDs with positive integer value.
   Negative or non-integer values will generate API errors."""

import json
import requests

BASE_URL = "https://petstore.swagger.io/v2"


# data = """{
#   "id": 0,
#   "petId": 123,
#   "quantity": 1,
#   "shipDate": "2018-12-31T08:23:29.842Z",
#   "status": "placed",
#   "complete": false
# }"""


class Store:
    """Creating class for POST, DELETE & GET methods."""
    def __init__(self):
        self.url = BASE_URL

    def storedelete(self, data, del_id):
        """POST before DELETE.
        We post data before delete."""
        data_json = json.loads(data)
        # print(data_json)
        resp = requests.post(BASE_URL + "/store/order", json=data_json)
        # print(resp)
        # print(resp.json())

        # """DELETE  Delete purchase order by ID.For valid response
        #  try integer IDs with positive integer value.
        #  Negative or non-integer values will generate API errors """
        response = requests.delete(BASE_URL + "/store/order/" + str(del_id))
        # print(response)

        # """check DELETE with GET"""
        response = requests.get(BASE_URL + "/store/order/" + str(del_id))
        # print(response)
        return response


# k = Store()
# k.storedelete("""{
#   "id": 11,
#   "petId": 13,
#   "quantity": 1,
#   "shipDate": "2018-12-31T08:23:29.842Z",
#   "status": "placed",
#   "complete": false
# }""", 11)
