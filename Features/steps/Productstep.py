import time

import allure
from behave import given, when, then
from Features.pages.LoginPage import LoginPage
from Features.pages.ProductPage import ProductPage

@allure.step(u'the user is on the login page')
@given(u'the user is on the login page')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.product = ProductPage(context.driver)
    context.login.open_login_page()

@allure.step(u'the user enters "{username}" and "{password}"')
@when(u'the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login.enter_username(username)
    context.login.enter_password(password)

@allure.step(u'clicks on login button')
@when(u'clicks on login button')
def step_impl(context):
    context.login.click_login_btn()

@allure.step(u'the user should be on the dashboard page')
@then(u'the user should be on the dashboard page')
def step_impl(context):
    context.login.validate_login_result("dashboard")

@allure.step(u'the shopping cart icon should be visible')
@then(u'the shopping cart icon should be visible')
def step_impl(context):
    assert context.product.cart_icon_is_vissible(), "Cart icon not visible"

@allure.step(u'the user selects 4 random products')
@when(u'the user selects 4 random products')
def step_impl(context):
     context.selected_products = context.product.select_random_products(4)

@allure.step(u'the product names should be displayed')
@then(u'the product names should be displayed')
def step_impl(context):

    for product in context.selected_products:
        print("Selected Product:", product)
