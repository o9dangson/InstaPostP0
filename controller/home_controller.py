from flask import request, render_template
from controller.logger_controller import log_get_req

def get_homepage():
    log_get_req('/', "render_template('index.html)")
    return render_template('index.html')