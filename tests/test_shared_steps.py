from pysst.steps.shared_steps import step_target_is

class behave_context(object):
    """Fake behave object"""
    def __init__(self):
        self.target = ""

def test_step_target_is():
    context = behave_context()
    step_target_is(context, '127.0.0.1')
    assert context.target == '127.0.0.1'
