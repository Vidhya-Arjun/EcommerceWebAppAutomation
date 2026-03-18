import time

from behave import *
from Features.pages.LoginPage import LoginPage


@given(u'User is in login page')
def step_impl(context):
    context.login = LoginPage(context.driver)

@when(u'User enters "{username}" and "{password}"')
def step_impl(context,username,password):
    context.login.enter_username(username)
    context.login.enter_password(password)


@when(u'Clicks on login button')
def step_impl(context):
    context.login.click_login_btn()


@then(u'"{result}" should be displayed')
def step_impl(context,result):
    context.login.validate_login_result(result)


@given(u'the user logs in with valid "{username}" and "{password}"')
def step_impl(context,username,password):
    context.login = LoginPage(context.driver)
    context.login.enter_username(username)
    context.login.enter_password(password)
    context.login.click_login_btn()
    time.sleep(5)


@then(u'the user should be on the "{result}" page')
def step_impl(context,result):
    context.login.validate_login_result(result)


@when(u'the user clicks on Logout')
def step_impl(context):
    context.login.click_logout_btn()


@then(u'the user should be redirected to the login page')
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/", "User not logged out properly, verify the logout steps"
    assert context.driver.get_cookie("session-username") is None, "Incorrect navigation"
