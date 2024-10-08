Feature: Login functionality

  Scenario: Successful login
    Given I navigate to the SauceDemo website
    When I log in with valid credentials
    Then I should be on the inventory page
