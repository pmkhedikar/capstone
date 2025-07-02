@apitest
Feature: Get user details from API

  Scenario: Verify GET API for user data
    When user send a GET request to "/api/users/2"
    Then the response code should be 200
    And the user details should be present:
      | email                  | first_name | last_name |
      | janet.weaver@reqres.in | Janet      | Weaver    |