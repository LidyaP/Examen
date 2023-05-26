Feature: Check if i can create my first Workspace

  @T3  @positiveTesting
  Scenario: I want to close the offer for Upgrade Now
    Given I am logged into my account
    When I see the upgrade offer modal
    When I click on x button
    Then The offer doesn't appear anymore


  @T4  @positiveTesting
  Scenario: I want to create my first Workspace
    When I click on add button
    When I insert my workspace name
    When I push the Create button
    Then My new workspace is created


  @T5   @positiveTesting
  Scenario: I am in my new Workspace and i want to close the DesignSpace Tour
    When I see the DesignSpace tour overlay
    When I close the DesignSpace tour
    Then The DesignSpace tour should be closed


  @T6   @positiveTesting
  Scenario: I am in my new Workspace and i want to create my first Wireframe
    When I chose the UI drawing add icon
    When I insert my Wireframe name
    When I search for my desired UI pack and i select it
    Then My Wireframe is created

  @T7  @positiveTesting
  Scenario: I am on my Wireframe and i want to add a template from store
    When From navigation bar i click on store icon
    When I am in store and i click on Templates bar
    When I click on the desired template and import it
    Then I can save my customized Wireframe


  @T8  @positiveTesting
  Scenario: I am in my new Workspace and i want to rename my Wireframe
    When I select from space settings the option Rename
    When I put the new name
    When I confirm the rename
    Then My Wireframe is renamed




