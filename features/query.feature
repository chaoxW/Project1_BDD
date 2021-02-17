Feature: Query validation
  # tests for home page
    Background: open login page
        Given launch chrome browser
        And open login page
        When insert username and password
        And click the login button
        Then User successfully login to the homepage

    Scenario Outline: query valid athlete from home page
        When I query with <athlete>
        Then I successfully go to the <athlete page>
        And close browser
        Examples:
            | athlete          | athlete page          |
            | Ronaldo Mulitalo | Ronaldo Mulitalo page |
            | Milan Hammond    | Milan Hammond page    |

    Scenario Outline: query invalid letters from home page
        When I query with <athlete>
        Then I unsuccessfully go to the <athlete page>
        And close browser
        Examples:
            | athlete | athlete page |
            | *       | * page       |
            | !       | ! page       |