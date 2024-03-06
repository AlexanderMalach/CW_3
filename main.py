from utils.class_Print_history import Print_history
from utils.functions import import_json
from utils.functions import print_sorted_list

sort_list = print_sorted_list()
list_dict = import_json()
for i in sort_list:
    copy = Print_history(list_dict(), i)
    print((
              f'\n{copy.date_print()} {copy.print_line('description')}\n{copy.account_code('from')} ->{copy.account_code('to')}\n{copy.currency()}\n'))
