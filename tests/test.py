from models.postcodes import PostCode
import json
data = """{
        "postcodes" : ["HA5 3WZ", "PA3 1RY", "NW7 2EY", "CB4 1HZ", "NE17 7SH"]
            }"""
dj = json.loads(data)
print(dj)
