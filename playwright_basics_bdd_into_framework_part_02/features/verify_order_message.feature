
Feature: Order ID verification for both UI and API
  This is a description about the feature file that we have here.
  This feature will log in and go to the order details page to verify the message
  Scenario Outline: Verify Order ID in the UI page
    Given place the <username> and <password> in login page from API
    And the user in on landing page

    When I log in with <username> and <password>
    And navigate to the order page
    And select the order ID

    Then the order ID should match with API order ID
    Examples:
      | username              | password     |
      | anshika@gmail.com     | Iamking@000 |