Feature:login functionality

@login
Scenario Outline: Login to Saucedemo Portal with different credentials
  Given User is in login page
  When User enters "<username>" and "<password>"
  And Clicks on login button
  Then "<result>" should be displayed

Examples:
  | username            | password   | result                  |
  | standard_user   | standard_user  | dashboard               |
  | locked_out_user | locked_out_user | error message          |
  |performance_glitch_user|secret_sauce|    dashboard          |
  |visual_user            |secret_sauce|  dashboard            |
  | problem_user          |secret_sauce |      dashboard       |
  