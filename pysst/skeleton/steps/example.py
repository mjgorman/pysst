from behave import given, when, then, step

@then('other will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.test_count >= 0

