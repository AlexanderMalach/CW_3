from utlis_.class_Print_history import Print_history
from utlis_.functions import print_sorted_list, import_json, check_error


def test_import_json():

    assert isinstance(import_json(), list)
    assert import_json()


# def test_print_sorted_list():
#     assert isinstance(functions.print_sorted_list({1:"01.01.2023"}[1], list))

def test_print_sorted_list():
    # data = [{"date": "01.01.2023"}, {"date": "02.01.2023"}, {"date": "03.01.2023"}, {"date": "04.01.2023"},
    #         {"date": "05.01.2023"}]

    # test_p = print_sorted_list(import_json_=data)
    assert isinstance(print_sorted_list(), list)


def test_check_error():
    assert check_error('test') == True
    assert check_error(None) == False