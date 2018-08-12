Feature: Example Feature

    Scenario: Request google's homepage
        Given requests is installed
        And the target of https://google.com
        When the request type is GET
        Then the status code is 200

    Scenario: Request google's homepage with the wrong host header
        Given requests is installed
        And the target of https://google.com
        When the request type is GET
        And we set the header host to mycoolsite.com
        Then the status code is 404
