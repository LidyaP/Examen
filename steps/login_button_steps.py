import password as password
from behave import *


@given("I am on the MockFlow homepage and i want to initiate the login process")
def step_impl(context):
    context.home_page.open_home_page()  #home_page este numele fisierului nu a clasei


@when("I enter my valid password")
def step_impl(context):
    context.home_page.insert_password()


@then("I am redirected to my account page")
def step_impl(context):
    context.home_page.my_account_page()


@given("I am on the MockFlow homepage and i want to initiate the login process with invalid password")
def step_impl(context):
    context.home_page.open_home_page()


@when("I click on login Button")
def step_impl(context):
    context.home_page.click_login_button()


@when("I enter my valid email")
def step_impl(context):
    context.home_page.insert_email()


@when('I enter my invalid "{user_password}"')
def step_impl(context,user_password):
    context.home_page.insert_invalid_password(user_password)


@when("I click on Sign In")
def step_impl(context):
    context.home_page.click_signin_button()


@then('I receive an "{error_message}"')
def step_impl(context,error_message):
    context.home_page.login_failed(error_message)
