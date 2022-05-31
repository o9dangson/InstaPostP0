from flask import request, render_template, redirect
from controller.logger_controller import log_get_req, log_post_req
from database.login_dao import select_login

def valid_input(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        if len(user) >= 1 and len(user) <=50 and len(pw) >= 1 and len(pw) <=50:
            return True
    else:
        return False

def is_valid_in_database(input):
    if 'username' in input and 'password' in input:
        user = input.get('username')
        pw = input.get('password')
        login_obj = select_login(user, pw)
        if login_obj is not None:
            return True
    return False

def get_login_err():
    log_get_req('/login/error', "render_template('index.html', method_used='GET')")
    return render_template('index.html', method_used='GET')

# Validate Login Obj
# Request User Obj
# Load Login page with User
def get_login_page(input):
    if valid_input(input) and is_valid_in_database(input):
        log_post_req('/login/input', f"redirect('/account/{input.get('username')}')")
        addr = f"/account/{input.get('username')}"
        return redirect(addr)
    else:
        log_post_req('/login/input', "redirect('/login/error')")
        return redirect('/login/error')
