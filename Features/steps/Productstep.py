import time


from behave import given, when, then
from Features.pages.LoginPage import LoginPage
from Features.pages.ProductPage import ProductPage


@given(u'the user is on the login page')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.product = ProductPage(context.driver)
    context.login.open_login_page()


@when(u'the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login.enter_username(username)
    context.login.enter_password(password)


@when(u'clicks on login button')
def step_impl(context):
    context.login.click_login_btn()


@then(u'the user should be on the dashboard page')
def step_impl(context):
    context.login.validate_login_result("dashboard")


@then(u'the shopping cart icon should be visible')
def step_impl(context):
    assert context.product.cart_icon_is_vissible(), "Cart icon not visible"


@when(u'the user selects 4 random products')
def step_impl(context):
     context.selected_products = context.product.select_random_products(4)


@then(u'the product names should be displayed')
def step_impl(context):

    for product in context.selected_products:
        print("Selected Product:", product)
