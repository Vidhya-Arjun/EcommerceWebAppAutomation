Feature:Cart functionality

@test_add_to_cart
Scenario: Add multiple products to cart
  Given the user is on the login page
  When the user enters "standard_user" and "secret_sauce"
  And clicks on login button
  Then the user should be on the dashboard page
  When the user adds below products to cart
    | productsname            |
    | Sauce Labs Backpack     |
    | Sauce Labs Onesie       |
    | Sauce Labs Bike Light   |
    | Sauce Labs Bolt T-Shirt |
  Then the cart icon count should be updated
  And the selected products should be added to the cart
