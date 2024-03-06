from utlis_.class_Print_history import Print_history
from utlis_.functions import import_json, print_sorted_list


# from class_Print_history import Print_history
# from functions import import_json, print_sorted_list

sort_list = print_sorted_list(Print_history)
for i in sort_list:
    copy = Print_history(import_json(), i)
    print((
        f'\n{copy.date_print()} {copy.print_line('description')}\n{copy.account_code('from')} ->{copy.account_code('to')}\n{copy.currency()}\n'))

