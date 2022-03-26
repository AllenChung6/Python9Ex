import os
import json


def read_json():
    file_path = os.path.abspath('mario.json')

    # opening JSON file
    f = open(file_path)

    # returns JSON object as dict
    data = json.load(f)
    return data
