import pytest
import datetime
from database.login_dao import *
from database.post_dao import *
from database.user_dao import *

# Testing Login
@pytest.mark.parametrize("test", [
    {'user': 'bobby1',
    'pw': 'pass1'},
    {'user': 'bob1',
    'pw': 'pass1'},
    {'user': 'bobby1',
    'pw': 'pass2'}, 
    {'user': '',
    'pw': 'pass3'},
])
def test_insert_login(test):
    #if test['user'] == 'bobby1' and test['pw'] == 'pass1':
    #    assert teardown() == True
    #    assert setup() == True
    result = insert_login(test['user'], test['pw'])
    if test['pw'] == 'pass2':
        assert result is None
    else:
        assert result is not None

@pytest.mark.parametrize("test", [
    {'user': 'bobby1',
    'pw': 'pass1'},
    {'user': 'bob1aslfijasfijalsijfalsiefjalsfijalsijefa;slfjasfelajsealifj;lf',
    'pw': 'pass1'},
    {'user': '',
    'pw': ';aliesfj;alisfej;alsifej;alsifejas;lfieeaj;slefalfieja;fias;a;fsea'},
])
def test_select_login(test):
    result = select_login(test['user'], test['pw'])
    if test['user'] == 'bobby1':
        assert result is not None
    else:
        assert result is None

@pytest.mark.parametrize("test", [
    {'id': '1', 'pw': 'pass1'},
    {'id': 'bobby1', 'pw': 'pass2'},
    {'id': 'bobby1', 'pw': ';aliesfj;alisfej;alsifej;alsifejas;lfieeaj;slefalfieja;fias;a;fsea'},
])
def test_select_login_by_id(test):
    result = select_login_by_id(test['id'])
    if(test['pw'] == 'pass1'):
        assert result is not None
    else:
        assert result is None


@pytest.mark.parametrize("test", [
    {'user': 'bobby1',
    'pw': 'pass1'},
    {'user': 'bob1',
    'pw': 'pass1'},
    {'user': 'aslfija;seifja;seifsja;efija;fiseaesfasefaefasefasfasefasfsefaefa',
    'pw': 'pass2'}, 
    {'user': '',
    'pw': 'pass3'},
])
def test_remove_login(test):
    result = remove_login('username', test['user'])
    assert result is True

# Testing User_info
@pytest.mark.parametrize("test",[
    {'f_name': 'Bobby', 'l_name': 'Bobberson'},
    {'f_name': 'Mat', 'l_name': 'Chitterbox'},
    {'f_name': 'Patrick', 'l_name': 'Star'}
])
def test_insert_user(test):
    result = insert_login(test['f_name'], test['l_name'])
    login_obj = select_login_by_id(result)
    if test['f_name'] == 'Mat':
        other_obj = select_login('Bobby', 'Bobberson')
        result = insert_user(login_obj.user_id, other_obj.user_id, test['f_name'], test['l_name'])
    else:
        result = insert_user(login_obj.user_id, login_obj.user_id, test['f_name'], test['l_name'])
    assert result is not None

@pytest.mark.parametrize("f_name, l_name, index",[
    ('Bobby', 'Bobberson', 5),
    ('Mat', 'Chitterbox',6),
    ('Patrick', 'Star',7)
])
def test_select_user(f_name, l_name, index):
    result = select_user_by_info_id(index-4)
    assert result.f_name == f_name and result.l_name == l_name
    result = select_user_by_user_id(index)
    assert result.f_name == f_name and result.l_name == l_name

@pytest.mark.parametrize("length, su_id",[
    (2, 5),
    (1, 7)
])
def test_select_by_super(length, su_id):
    results = select_user_by_superUser(su_id)
    assert len(results) == length

@pytest.mark.parametrize("su_id",[
    5, 7
])
def test_remove(su_id):
    result = remove_user_info('super_user_id', su_id)
    assert result == True

# Testing Posts
now = datetime.datetime.now().strftime('%Y-%m-%d')
@pytest.mark.parametrize("test",[
    {'u_id': 5, 'title': '5', 'desc': 'Description', 'date': now},
    {'u_id': 6, 'title': '6', 'desc': 'Description', 'date': now},
    {'u_id': 7, 'title': '7', 'desc': 'Description', 'date': now}
])
def test_insert_post(test):
    result = insert_post(test['u_id'], test['title'], test['desc'], test['date'])
    assert result is not None

@pytest.mark.parametrize("post_id, user_id",[
    (1, 5), (2, 6), (3, 7)
])
def test_post_func(post_id, user_id):
    post_obj = select_post_by_post_id(post_id)
    assert post_obj.user_id == user_id
    list = select_post_list_by_user_id(user_id)
    assert list[0].post_id == post_id
    post_obj = update_post(post_obj)
    assert post_obj == True
    post_obj = remove_post('user_id', user_id)
    assert post_obj == True
