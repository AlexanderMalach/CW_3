import json


def import_json():
    with open('operations.json', 'r', encoding='utf-8') as file:
        return json.load(file)
