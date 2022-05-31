from flask import request, render_template, redirect
from controller.logger_controller import log_get_req, log_post_req
from database.login_dao import select_login_by_id, select_login_by_user
from database.post_dao import *
import datetime

from database.user_dao import select_user_by_info_id, select_user_by_user_id

def get_page(user):
    login_obj = select_login_by_user(user)
    list_post = select_post_list_by_user_id(login_obj.user_id)
    user_obj = select_user_by_user_id(login_obj.user_id)
    login_obj = select_login_by_id(user_obj.superUser_id)
    return render_template('user.html', username=user, super_user=login_obj.user, list=list_post)

def get_user_page(user):
    log_get_req(f'/account/{user}/posts', f"render_template('user.html', username={user}, super_user=login_obj.user, list=list_post)")
    return get_page(user)

def create_post(user, input):
    login_obj = select_login_by_user(user)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    post_id = insert_post(login_obj.user_id, input.get('title'), input.get('desc'), now)
    log_post_req(f'/post/{user}/add', f"render_template('user.html', username={user}, super_user=login_obj.user, list=list_post)")
    return get_page(user)

def delete_post(user, post_id):
    #Update DB
    result = remove_post('post_id', post_id)
    log_get_req(f'/post/{user}/delete/{post_id}', f"render_template('user.html', username={user}, super_user=login_obj.user, list=list_post)")
    return get_page(user)

def get_update_post_page(user, post_id):
    post_obj = select_post_by_post_id(post_id)
    log_get_req(f"/post/{user}/update/{post_id}", f"render_template('update.html', post_obj={post_obj}, username={user})")
    return render_template('update.html', post_obj=post_obj, username=user)

def update_post_page(input):
    post_id = input.get('post_id')
    user = input.get('username')
    post_date = input.get('post_date')
    post_title = input.get('title')
    post_desc = input.get('desc')
    login_obj = select_login_by_user(user)
    post_obj = Post(post_id, login_obj.user_id,post_title, post_desc, post_date)
    result = update_post(post_obj)
    log_post_req(f"/post/update", f"render_template('update.html', post_obj={post_obj}, username={user})")
    return get_page(input.get('username'))