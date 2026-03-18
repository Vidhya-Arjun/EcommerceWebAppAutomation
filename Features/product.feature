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


@test_add_to_cart
Scenario Outline: Add selected products to cart and validate
  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks on login button
  Then the user should be on the dashboard page
  When the user selects 4 random products and adds to cart
  Then the cart icon count should be 4
  And the selected products should be present in the cart

Examples:
  | username       | password      |
  | standard_user  | secret_sauce  |
