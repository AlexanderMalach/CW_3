import json


def import_json():
    """ Открывает json объект и возвращает его"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def check_error(word):
    """ Проверка на наличие ключа в словаре, возвращает False
или True """
    if word == None:
        print("Что-то не так с ключом :(\nКакое-то значение будет \'None\' ")
        return False
    else:
        return True
