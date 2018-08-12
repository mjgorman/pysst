from behave import given, when, then, step

@given('the target of {target}')
def step_target_is(context, target):
    context.target = target
