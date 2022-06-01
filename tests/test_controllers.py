import pytest

from controller.login_controller import valid_input
from controller.registration_controller import *
from controller.user_controller import *

#Account Controller functions only use database functions.
#Tested in test_database.py

#Home Ctrler too simplistic. No test needed.

#Logger Tests are in test_class.py
@pytest.mark.parametrize("test",[
    {'username': 'test1', 'password': 't'},
    {'username': 'test2', 'password': ''},
    {'username': '', 'password': 'test3'},
    {'user': 'test4', 'password': '222222222222222222222'}
])
def test_valid_input(test):
    result = False
    if 'username' in test and 'password' in test:
        result = valid_input(test)
        if test.get('username') == '' or test.get('password') == '':
            assert result == False
        else:
            assert result == True
    else:
        assert result == False

#Registration uses same functions

#User controller uses database functions