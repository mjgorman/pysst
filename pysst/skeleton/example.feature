Feature: Example Feature

    Scenario: Run an nmap port scan on examples
        Given nmap is installed
        And the target of 127.0.0.1
        When we scan port 1313
        Then nmap will show closed

