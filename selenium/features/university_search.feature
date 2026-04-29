# language: en
Feature: University Search Navigation

  As a user
  I want to search for universities and explore their programs
  So that I can validate their academic offerings

  Scenario Outline: Search university and validate careers page
    Given I am on the Google homepage
    When I search for "<query>"
    And I click the first result
    Then I should be on "<expected_domain>"
    When I search "<term>" inside the site
    Then I should see results related to "<term>"

  Examples:
    | query   | expected_domain | term     |
    | iteso   | iteso.mx        | carreras |
    | unam    | unam.mx         | carreras |
    | udg     | udg.mx          | carreras |
