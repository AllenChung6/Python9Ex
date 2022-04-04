import os
import json
import pickle


# Part A
def read_json(directory, file_name):
    # opening JSON file
    with open(os.path.join(directory, file_name), 'r') as file:
        # returns JSON object as dict
        data = json.load(file)
    return data


# Part B
def read_all_json_files(directory, file_name):
    # file_path1 = '/Users/allenc/PyCharmProjects/Python9Ex/data/super_smash_bros/link.json'
    list_of_files = []
    for file_name in os.listdir(directory):
        read_json(directory, file_name)
        data = read_json(directory, file_name)
        list_of_files.append(data)

    return list_of_files


# Part C
def write_pickle(directory):
    pickle_file = open('super_smash_characters.pickle', 'wb')
    pickle.dump(directory, pickle_file)


write_pickle('/Users/allenc/PyCharmProjects/Python9Ex/data/')
print(read_all_json_files('/Users/allenc/PyCharmProjects/Python9Ex/data/super_smash_bros', 'link.json'))

