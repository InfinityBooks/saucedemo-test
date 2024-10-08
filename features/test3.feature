Feature: Negative login functionality

  Scenario: Unsuccessful login
    Given I navigate to the SauceDemo website
    When I log in with invalid credentials
    Then I should see an error message
