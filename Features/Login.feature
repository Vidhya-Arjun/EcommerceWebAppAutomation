Feature:login functionality

@valid-login
Scenario Outline: Login to Saucedemo Portal with different credentials
  Given User is in login page
  When User enters "<username>" and "<password>"
  And Clicks on login button
  Then "<result>" should be displayed

Examples:
  | username            | password   | result                  |
  | standard_user   | secret_sauce  | dashboard               |
  | locked_out_user | secret_sauce | error message          |
  |performance_glitch_user|secret_sauce|    dashboard          |
  |visual_user            |secret_sauce|  dashboard            |
  | problem_user          |secret_sauce |      dashboard       |
  | error_user          |secret_sauce |      dashboard       |

@invalid-login
Scenario Outline: Login to Saucedemo with Invalid credential
  Given User is in login page
  When User enters "<username>" and "<password>"
  And Clicks on login button
  Then "<result>" should be displayed

Examples:
  | username            | password   | result                  |
  | Jeevan   | secret_sauce  | error message                |

@validate-logout
Scenario Outline: Validate logout functionality
  Given the user logs in with valid "<username>" and "<password>"
  Then the user should be on the "<result>" page
  When the user clicks on Logout
  Then the user should be redirected to the login page

  Examples:
  | username       | password      | result |
  | standard_user  | secret_sauce  |dashboard|


