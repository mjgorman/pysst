Feature: Check ports are closed

    Scenario Outline: Run an nmap port scan on examples
        Given nmap is installed
        And the target of 127.0.0.1
        When we scan port <port>
        Then nmap will show closed

        Examples: Ports
          | port |
          | 80   |
          | 443  |
          | 1313 |
