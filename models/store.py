import requests
import json
import logging

""" Configure logger """
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
file_handler = logging.FileHandler('store.log')  # Save log to file
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


BASE_URL = 'http://petstore.swagger.io/v2'


class Store:
    def __init__(self):
        self.response = requests.get(BASE_URL + '/store/inventory')

    def get_inventory(self):
        if self.response.status_code == 200:
            logger.info(f'Status code: {self.response.status_code}.')
            return json.dumps(self.response.json(), indent=4)
        else:
            logger.debug('Something went wrong')

    @staticmethod
    def order(j_inp):
        data_json = json.loads(j_inp)
        resp = requests.post(BASE_URL + "/store/order", json=data_json)
        print(resp.json())


r = requests.get(BASE_URL+'/store/inventory')

# print(r.status_code)
# print(r.json())
# print(r.content)
res = Store()

print(res.get_inventory())

