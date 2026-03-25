
from behave import when, then
from Features.pages.CartPage import CartPage
import math


@when('the user adds below products to cart')
def step_impl(context):
    context.cart = CartPage(context.driver)
    context.selected_products = []

    for row in context.table:
        product = row['productsname']
        context.cart.add_products_tocart(product)
        context.selected_products.append(product)

@then('the cart icon count should be updated')
def step_impl(context):
    count = context.cart.get_cart_count()
    assert int(count) == len(context.selected_products)

@then(u'the selected products should be added to the cart')
def step_impl(context):
    context.cart.open_cart()
    cart_items = context.cart.get_cart_item_names()

    for product in context.selected_products:
        assert product in cart_items, f"{product} not found in cart"


