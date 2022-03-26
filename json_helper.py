import os
import json


# Part A
def read_json(file_path):
    # opening JSON file
    f = open(file_path)

    # returns JSON object as dict
    data = json.load(f)
    return data


# Part B
def read_all_json_files():
    file_path = '/Users/allenc/PyCharmProjects/Python9Ex/data/super_smash_bros/mario.json'
    file_path1 = '/Users/allenc/PyCharmProjects/Python9Ex/data/super_smash_bros/link.json'

    obj1 = read_json(file_path)
    obj2 = read_json(file_path1)

    list_of_files = [obj1, obj2]
    return list_of_files


print(read_all_json_files())

