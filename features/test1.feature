Feature: Verify landing page

  Scenario: Navigate to the website and verify the landing page
    Given I navigate to the SauceDemo website
    Then I should see the correct landing page title
