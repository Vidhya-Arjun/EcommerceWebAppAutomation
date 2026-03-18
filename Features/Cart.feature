Feature:Cart functionality

@test_add_to_cart
Scenario Outline: Add selected products to cart and validate
  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks on login button
  Then the user should be on the dashboard page
  When the user selects products and adds them to the cart
    | name          | price  | quantity |
    | Laptop        | 999.99 | 1        |
    | USB Cable     | 15.00  | 2        |
  Then the cart icon count should be updated
  And the selected products should be added to the cart

Examples:
  | username      | password     |
  | standard_user | secret_sauce |