from pysst.steps.nmap_steps import step_nmap_is_installed, step_we_scan_port, step_nmap_will_show_desired
import nmap

class behave_context(object):
    """Fake behave object"""
    def __init__(self):
        self.scanner = None
        self.target = '127.0.0.1'
        self.port = 0

def test_step_nmap_is_installed():
    context = behave_context()
    step_nmap_is_installed(context)
    assert context.scanner is not None

def test_step_we_scan_port():
    context = behave_context()
    step_we_scan_port(context, '1313')
    assert context.port is '1313'

def test_step_nmap_will_show_disired():
    context = behave_context()
    context.port = '1313'
    context.scanner = nmap.PortScanner()
    step_nmap_will_show_desired(context, 'closed')
