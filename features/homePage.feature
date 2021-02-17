Feature: Home Page validation
  # tests for home page
    Background: open login page
        Given launch chrome browser
        And open login page
        When insert username and password
        And click the login button
        Then User successfully login to the homepage

    Scenario Outline: Validate the menu of home page
        When I click <menu>
        Then I successfully go to the <page>
        And close browser

        Examples:
            | menu          | page                 |
            | Home          | Home page            |
            | Explore       | Explore page         |
            | Notifications | Notification content |
            | Messages      | Messages App         |
            | Account       | User Menu            |