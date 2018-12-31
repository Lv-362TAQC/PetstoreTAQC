import requests
import json
import logging
import os.path

""" Configure logger """
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
                              datefmt='%d/%m/%Y %H:%M:%S')
if not os.path.exists("logs/"):
    os.makedirs("logs/")
file_handler = logging.FileHandler(f'logs/{logger.name}.log')  # Save log to file
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


BASE_URL = 'http://petstore.swagger.io/v2'


class Store:
    def __init__(self):
        self.url = BASE_URL + '/store'

    def get_inventory(self):
        response = requests.get(self.url + '/inventory')
        status_code = response.status_code
        if status_code == 200:
            logger.info(f'Status code: {status_code}. Successful operation.')
            return json.dumps(response.json(), ensure_ascii=False, indent=4)
        else:
            logger.debug(f'Status code: {status_code}. Something went wrong')

    def order(self, j_inp):
        data_json = json.loads(j_inp)
        try:
            response = requests.post(self.url + "/order", json=data_json)
            # print(response.content, response.headers['content-type'])
        except:
            logger.debug(f'{response.status_code}')
        finally:
            return response


res = Store()

print(res.get_inventory())
data = """{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2018-12-31T19:27:34.759Z",
  "status": "placed",
  "complete": false
}"""

print(res.order(data).text)
print(res.order(data).headers['content-type'])
