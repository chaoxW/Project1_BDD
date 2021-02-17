Feature: Login Page validation
  # tests for login page
    Background: open login page
        Given launch chrome browser
        And open login page

    Scenario: Log in with valid user name and password
        When insert username and password
        And click the login button
        Then User successfully login to the homepage
        And close browser


    Scenario: Log in with invalid user name and password
        When insert invalid username and password
        And click the login button
        Then User unsuccessfully login to the homepage
        And close browser