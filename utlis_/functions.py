import datetime
import json



def import_json():
    """ Открывает json объект и возвращает его"""
    # with open('operations.json', 'r', encoding='utf-8') as file:
    with open('C:\\Users\\79096\\PycharmProjectsGit\\CW_3\\CW_3\\utlis_\\operations.json', 'r', encoding='utf-8') as file:

        return json.load(file)

def check_error(word):
    """ Проверка на наличие ключа в словаре, возвращает False
или True """
    if word == None:
        print("Что-то не так с ключом :(\nКакое-то значение будет \'None\' ")
        return False
    else:
        return True


def print_sorted_list(Print_history_, min_range=0, max_range=5):
    """ Сортировка по убыванию дат, возварщает отсортированный список индексов,
    который используеться для создания экземпляров по убыванию дат """

    list_sort = list()
    for i in range(min_range, max_range):
        copy_print_history = Print_history_(import_json(), i)
        d = (copy_print_history.date_print())
        list_sort.append(d)
    sorted_values = sorted(list_sort, key=lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"), reverse=True)
    list_index = list()
    for v in list_sort:
        a = (sorted_values.index(v))
        list_index.append(a)

    return (list_index)
