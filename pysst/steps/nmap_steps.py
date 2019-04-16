from behave import given, when, then, step


@given('nmap is installed')
def step_nap_is_installed(context):
    import nmap
    context.scanner = nmap.PortScanner()

@when('we scan port {port}')
def step_we_scan_port(context, port):
    context.port = port

@then('nmap will show closed')
def step_nmap_will_show_closed(context):
    context.scanner.scan(context.target, context.port)
    state = context.scanner[context.target]['tcp'][int(context.port)]['state']
    assert state == "closed"

@then('nmap will show open')
def step_nmap_will_show_closed(context):
    context.scanner.scan(context.target, context.port)
    state = context.scanner[context.target]['tcp'][int(context.port)]['state']
    assert state == "open"

