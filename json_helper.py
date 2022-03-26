import os
import json


# Part A
def read_json(file_path):
    file_path = os.path.abspath('mario.json')

    # opening JSON file
    f = open(file_path)

    # returns JSON object as dict
    data = json.load(f)
    return data


# Part B
def read_all_json_files():
    file_path = os.path.abspath('mario.json')
    file_path1 = os.path.abspath('link.json')
    file_path2 = os.path.abspath('superman.json')
    file_path3 = os.path.abspath('thor.json')
    file_path4 = os.path.abspath('goku.json')
    file_path5 = os.path.abspath('krillin.json')

    obj1 = read_json(file_path)
    obj2 = read_json(file_path1)
    obj3 = read_json(file_path2)
    obj4 = read_json(file_path3)
    obj5 = read_json(file_path4)
    obj6 = read_json(file_path5)

    list_of_files = [obj1, obj2, obj3, obj4, obj5, obj6]
    return list_of_files

