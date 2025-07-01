@login

  Feature: User login functionality

    @loginUser
    Scenario: Successful user login to application
      Given the user is on the login page
      When the user enter username and password
      Then the user land on the dashboard page

    @invalid_user
    Scenario Outline: Verify error message for login with incorrect credentials
      Given the user is on the login page
      When the user enter the <username> and <password>
      Then the <error message> is displayed

    Examples:
      |username      |password         | error message                                                              |
      |standard_user |invalid_password | Epic sadface: Username and password do not match any user in this service  |
      |InvalidUser   |secret_sauce     | Epic sadface: Username and password do not match any user in this service  |