from pysst.steps.requests_steps import step_requests_is_installed, step_we_set_header, step_the_request_type_is, step_status_code_is
import requests

class behave_context(object):
    """Fake behave object"""
    def __init__(self):
        self.requests = None
        self.request_type = 'get'
        self.target = None
        self.headers = {}

def test_step_requests_is_installed():
    context = behave_context()
    step_requests_is_installed(context)
    assert context.requests is requests

def test_step_we_set_header():
    context = behave_context()
    step_we_set_header(context, 'host', 'localhost')
    assert context.headers['host'] == 'localhost'

def test_step_the_request_type_is_post():
    context = behave_context()
    step_the_request_type_is(context, 'post')
    assert context.request_type == 'post'

def test_step_status_code_is():
    context = behave_context()
    context.target = "https://google.com"
    context.requests = requests
    step_status_code_is(context, 200)
