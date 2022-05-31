from models.logger import Logger
import datetime

from tests.test_class import my_logger

def setup_logger_obj():
    my_logger = Logger('logs.txt')
    my_logger.setup()

def log_get_req(route, result):
    my_logger = Logger('logs.txt')
    my_logger.log_change('GET', route, result)

def log_post_req(route, result):
    my_logger = Logger('logs.txt')
    my_logger.log_change('POST', route, result)