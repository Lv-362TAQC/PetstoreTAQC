import requests
import json
import logging
import os.path
# import http
#
# print(http.HTTPStatus)


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


BASE_URL = 'https://api.exchangeratesapi.io'
OK = 200


class Latest:
    def __init__(self):
        self.url = BASE_URL + '/latest'


    def latest_foreign(self):
        response = requests.get(self.url)
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url}")
        else:
            logger.debug(f'Status code: {status_code}. Something wrong. URL: {self.url}')
            print(f'Code status: {status_code}. Something wrong. URL: {self.url}')
        return response


    def latest_base(self):
        response = requests.get(self.url + '?base=USD')
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url + '?base=USD'}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url + '?base=USD'}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url + '?base=USD'}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url + '?base=USD'}")
        return response


    def latest_sumbols(self):
        response = requests.get(self.url + '?symbols=USD,GBP')
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url + '?symbols=USD,GBP'}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url + '?symbols=USD,GBP'}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url + '?symbols=USD,GBP'}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url + '?symbols=USD,GBP'}")
        return response

class Day:
    def __init__(self):
        self.url = BASE_URL + '/2010-01-12'

    def historical(self):
        response = requests.get(self.url)
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url}")
        return response


class History:
    def __init__(self):
        self.url = BASE_URL + '/history'

    def rates_time_period(self):
        response = requests.get(self.url + '?start_at=2018-01-01&end_at=2018-09-01')
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01'}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01'}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01'}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01'}")
        return response

    def specific_exchange_rates(self):
        response = requests.get(self.url + '?base=USD')
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY'}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY'}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY'}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&symbols=ILS,JPY'}")
        return response

    def different_currency(self):
        response = requests.get(self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD')
        status_code = response.status_code
        if status_code == OK:
            logger.info(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD'}")
            print(f"Code status: {status_code}. Successful operation. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD'}")
        else:
            logger.debug(f"Status code: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD'}")
            print(f"Code status: {status_code}. Something wrong. URL: {self.url + '?start_at=2018-01-01&end_at=2018-09-01&base=USD'}")
        return response

    # def post_createWithArray(self, resp_body):
    #     data_json = json.loads(resp_body)
    #     try:
    #         response = requests.post(self.url + "/createWithArray", json=data_json)
    #         logger.info(f"{response.content, response.headers['content-type']}")
    #         print(response.content, response.headers['content-type'])
    #     except:
    #         logger.info(f'{response.status_code}')
    #         print(f'{response.status_code}')
    #     finally:
    #         return response


res = Latest()
d = res.latest_foreign().text
h = res.latest_base().text
w = res.latest_sumbols().text

res = Day()
u = res.historical().text

res = History()
p = res.rates_time_period().text
n = res.specific_exchange_rates().text
z = res.different_currency().text
# s = json.loads(d)
# print(s)
# print(s["rates"]["HRK"])
# data = """[{
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }]"""
#
# res.post_createWithArray(data)
#
#
# data_json = json.loads(data)
# resp = requests.post(BASE_URL + "/user/createWithArray", json=data_json)
# print(resp.json())
