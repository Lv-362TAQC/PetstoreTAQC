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


BASE_URL = 'https://petstore.swagger.io/v2/store'


class Store:
    def __init__(self):
        self.url = BASE_URL

    def get_inventory(self):
        response = requests.get(self.url + '/inventory')
        status_code = response.status_code
        if status_code == 200:
            logger.info(f'Status code: {status_code}. Successful operation.')
            return response # json.dumps(response.json(), ensure_ascii=False, indent=4)
        else:
            logger.debug(f'Status code: {status_code}. Something went wrong')
            return response

    def order(self, j_inp):
        data_json = json.loads(j_inp)
        try:
            response = requests.post(self.url + "/order", json=data_json)
            # print(response.content, response.headers['content-type'])
        except:
            logger.exception(f'{response.status_code}')
        finally:
            return response.json()

    def check_order(self, order_id):
        response = requests.get("https://petstore.swagger.io/v2/store/order/"+order_id)
        return response.json()

    def del_order(self, order_id):
        response = requests.delete(self.url+f"/order/{order_id}")
        return response
