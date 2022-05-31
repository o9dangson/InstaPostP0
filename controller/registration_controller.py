from flask import request, render_template, redirect
from controller.logger_controller import log_get_req, log_post_req
from database.login_dao import select_login, insert_login, select_login_by_id, select_login_by_user
from database.user_dao import insert_user, select_user_by_user_id

def get_register_page():
    log_get_req('/register', "render_template('register.html', error=None)")
    return render_template('register.html', error=None)

def get_register_page2(user):
    log_get_req('/register/user', "render_template('register_2.html', error=None)")
    return render_template('register_2.html', error=None, username=user)
    
def get_register_err():
    log_get_req('/register/error', "render_template('register.html', error='POST')")
    return render_template('register.html', error='POST')

def get_register_err2():
    log_get_req('/register/user/error', "render_template('register_2.html', error='POST')")
    return render_template('register_2.html', error='POST')

def is_valid_in_database(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        login_obj = select_login_by_user(user)
        if login_obj is None:
            return True
    return False

def valid_input(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        if len(user) >= 1 and len(user) <=50 and len(pw) >= 1 and len(pw) <=50:
            return True
    print( f"user: {len(user)}\t pw: {len(pw)}")
    return False

def add_account(input):
    user = input.get('username')
    pw = input.get('password')
    f_name = input.get('f_name')
    l_name = input.get('l_name')
    insert_login(user, pw)
    user_login = select_login(user, pw)
    insert_user(user_login.user_id, user_login.user_id, f_name, l_name)

def add_account2(input, user2):
    user = input.get('username')
    pw = input.get('password')
    f_name = input.get('f_name')
    l_name = input.get('l_name')
    login_id = insert_login(user, pw)
    super_login = select_login_by_user(input.get('super_user'))
    info_id = insert_user(login_id, super_login.user_id, f_name, l_name)
    login_obj = select_login_by_user(user2)

def attempt_registration(input):
    if valid_input(input) and is_valid_in_database(input):
        add_account(input)
        log_post_req('/register/input', "redirect('/')")
        return redirect('/')
    else:
        log_post_req('/register/input', "redirect('/register/error')")
        return redirect('/register/error')

def attempt_registration2(input):
    if valid_input(input) and is_valid_in_database(input):
        add_account2(input, input.get('super_user'))
        login_obj = select_login_by_user(input.get('super_user'))
        log_post_req('/register/user/input', f"redirect('/account/{login_obj.user}')")
        return redirect(f'/account/{login_obj.user}')
    else:
        print( valid_input(input))
        print( is_valid_in_database(input))
        log_post_req('/register/user/input', "redirect('/register/user/error')")
        return redirect('/register/user/error')