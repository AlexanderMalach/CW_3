import json


def import_json():
    with open('operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def check_error(word):
    if word == None:
        print("Что-то не так с ключом :(\nКакое-то значение будет \'None\' ")
        return False
    else:
        return True
