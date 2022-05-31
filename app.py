from re import T
from flask import Flask, request
#from database.login_dao import *
from controller.home_controller import get_homepage
from controller.login_controller import *
from controller.registration_controller import *
from controller.logger_controller import *
from controller.account_controller import *
from controller.user_controller import *


class App:
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        return get_homepage()
    
    @app.route('/register', methods=['GET'])
    def register():
        return get_register_page()
    
    @app.route('/register/input', methods=['POST'])
    def register_input():
        return attempt_registration(request.form)

    @app.route('/register/error', methods=['GET'])
    def register_err():
        return get_register_err()
    
    @app.route('/register/<user>', methods=['GET'])
    def register2(user):
        return get_register_page2(user)
    
    @app.route('/register/user/input', methods=['POST'])
    def register_user_input():
        return attempt_registration2(request.form)

    @app.route('/register/user/error', methods=['GET'])
    def register_err2():
        return get_register_err2()

    @app.route('/login/error', methods=["GET"])
    def login_err():
        return get_login_err()

    @app.route('/login/input', methods=['POST'])
    def login():
        return get_login_page(request.form)

    @app.route('/account/<user>', methods=['GET'])
    def account(user):
        return get_account_page(user)

    @app.route('/account/<user>/posts', methods=['GET'])
    def user_page(user):
        return get_user_page(user)

    @app.route('/account/delete/<user>', methods=['GET'])
    def delete_user(user):
        return remove_user(user)

    @app.route('/account/close/<user>', methods=['GET'])
    def close_account(user):
        return remove_all_users(user)

    @app.route('/post/<user>/add', methods=['POST'])
    def add_new_post(user):
        return create_post(user, request.form)

    @app.route('/post/<user>/update/<post_id>', methods=['GET'])
    def update_post_page(user, post_id):
        return get_update_post_page(user, post_id)

    @app.route('/post/<user>/delete/<post_id>', methods=['GET'])
    def delete_post_page(user, post_id):
        return delete_post(user, post_id)

    @app.route('/post/update', methods=['POST'])
    def updating_post():
        return update_post_page(request.form)

if __name__ == '__main__':
    setup_logger_obj()
    App.app.run(debug=True)