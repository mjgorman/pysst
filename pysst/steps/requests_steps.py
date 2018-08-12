from behave import given, when, then, step

@given('requests is installed')
def step_requests_is_installed(context):
    import requests
    context.requests = requests
    context.headers = {}

@when('we set the header {header} to {value}')
def step_we_set_header(context, header, value):
    context.headers[header] = value

@when('the request type is {request_type}')
def step_the_request_type_is(context, request_type):
    context.request_type = request_type.lower()

@then('the status code is {status_code:d}')
def step_nmap_will_show_closed(context, status_code):
    if context.request_type == 'get':
        r = context.requests.get(context.target, headers=context.headers)
    if context.request_type == 'post':
        r = context.requests.post(context.target, headers=context.headers)
    print(r.status_code)
    assert r.status_code == status_code
