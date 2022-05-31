from flask import request, render_template, redirect
from controller.logger_controller import log_get_req
from database.user_dao import *
from database.login_dao import *
from database.post_dao import *

def get_account_page(user):
    login_obj = select_login_by_user(user)
    user_obj = select_user_by_user_id(login_obj.user_id)
    list_user = select_user_by_superUser(user_obj.superUser_id)
    list_login= []
    for user_info in list_user:
        login_obj = select_login_by_id(user_info.user_id)
        list_login.append(login_obj.user)
    log_get_req(f'/account/{user}', f"render_template('account.html', username={user}, list=list)")
    return render_template('account.html', username=user, list=list_login)

def remove_from_database(user):
    login_obj = select_login_by_user(user)
    result = remove_post('user_id', login_obj.user_id)
    result = remove_user_info('user_id', login_obj.user_id)
    result = remove_login('user_id', login_obj.user_id)
    return result

def remove_all_users(user):
    login_obj = select_login_by_user(user)
    user_obj = select_user_by_user_id(login_obj.user_id)
    list_users = select_user_by_superUser(user_obj.superUser_id)
    for user in list_users:
        login_obj = select_login_by_id(user.user_id)
        remove_from_database(login_obj.user)
    log_get_req(f'/account/close/{user}', "redirect('/')")
    return redirect('/')

def remove_user(user):
    login_obj = select_login_by_user(user)
    user_obj = select_user_by_user_id(login_obj.user_id)
    super_user_id = user_obj.superUser_id
    if user_obj.superUser_id == login_obj.user_id:
        return remove_all_users(user)
    else:
        login_obj = select_login_by_id(super_user_id)
        result = remove_from_database(user)
        log_get_req(f'/account/delete/{login_obj.user}', f"return redirect(f'/account/{login_obj.user}')")
        return redirect(f'/account/{login_obj.user}')