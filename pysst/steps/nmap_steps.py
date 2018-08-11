from behave import given, when, then, step
import nmap

@given('nmap is installed')
def step_nap_is_installed(context):
    context.scanner = nmap.PortScanner()

@given('the target of {target}')
def step_target_is(context, target):
    context.target = target

@when('we scan port {port}')
def step_we_scan_port(context, port):
    context.port = port

@then('nmap will show closed')
def step_nmap_will_show_closed(context):
    context.scanner.scan(context.target, context.port)
    state = context.scanner[context.target]['tcp'][int(context.port)]['state']
    print(state)
    assert state == "closed"

