Feature:product functionality

@validate-cart_icon_visibility
Scenario Outline: Shopping cart icon is visible on dashboard
  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks on login button
  Then the user should be on the dashboard page
  And the shopping cart icon should be visible

Examples:
  | username            | password   |
  | standard_user   | secret_sauce  |

@test_display_name
Scenario Outline: Select 4 random products and display names
  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks on login button
  Then the user should be on the dashboard page
  When the user selects 4 random products
  Then the product names should be displayed

Examples:
  | username            | password   |
  | standard_user   | secret_sauce  |


Scenario: Complete checkout and validate orderWhen the user proceeds to checkout

  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks on login button
  Then the user should be on the dashboard page
  When the user selects random products

  And the user fills in checkout details
    | first_name | last_name | postal_code |
    | John       | Doe       | 12345       |
  Then the order summary should reflect correct product data
  And the user should receive a confirmation message
