from utlis.f import check_error
from utlis.class_Print_history import Print_history


def test_check_error():
    assert check_error('test_utlis') == True
    assert check_error(None) == False
