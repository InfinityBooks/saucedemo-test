Feature: Checkout process

  Scenario: Successful checkout
    Given I navigate to the SauceDemo website
    When I log in with valid credentials
    And I add two items to the cart
    And I proceed to checkout
    Then I should see a confirmation message
