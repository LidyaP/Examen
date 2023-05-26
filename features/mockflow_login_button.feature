Feature: Check that the login button in the MockFlow website is working properly and i can access my account

  @T1  @negativeTesting
  Scenario: Trying to login with invalid password
    Given I am on the MockFlow homepage and i want to initiate the login process with invalid password
    When I click on login Button
    When I enter my valid email
    When I enter my invalid password
    When I click on Sing In
    Then I receive an error message

  @T2   @positiveTesting
  Scenario: Clicking on the login button
    When I click on login Button
    When I enter my valid email
    When I enter my valid password
    When I click on Sing In
    Then I am redirected to my account page







