from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):
    assert number > 1 or number == 0
    context.test_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.test_count >= 0
