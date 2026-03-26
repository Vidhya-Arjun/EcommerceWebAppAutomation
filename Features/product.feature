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
 Scenario Outline: Complete checkout and validate order
    Given the user is logged into the application with "<username>" and "<password>"
    And the user has added products to the cart
    When the user navigates to the cart page
    And the user clicks on the checkout button
    And the user enters "<first_name>" "<last_name>" and "<postal_code>"
    And the user proceeds to the order summary page
    Then the order summary should display correct product details
    And the user captures a screenshot of the order summary
    When the user clicks on finish
    Then the user should see the order confirmation message "<message>"

    Examples:
      | username      | password     | first_name | last_name | postal_code | message                    |
      | standard_user | secret_sauce | Vidhya     | Arjun     | 600001      | Thank you for your order! |


   Feature: Product sorting functionality

  Scenario: Validate sorting on products page
    Given the user is on the login page
    When the user enters "standard_user" and "secret_sauce"
    And clicks on login button
    When the user selects "Price (low to high)" from the sort dropdown
    Then the product list should be sorted in ascending order of price

    When the user selects "Name (Z to A)" from the sort dropdown
    Then the product list should be sorted in descending alphabetical order


Feature: Reset App State functionality

  Scenario Outline: Validate Reset App State functionality
    Given the user is logged into the application with "<username>" and "<password>"
    And the user adds "<product_count>" products to the cart
    When the user opens the menu
    And the user clicks on "Reset App State"
    Then the cart icon count should be "<expected_count>"
    And no products should remain in the cart

    Examples:
      | username      | password     | product_count | expected_count |
      | standard_user | secret_sauce | 3             | 0              |
      | standard_user | secret_sauce | 5             | 0              |