from behave import given, when, then
from playwright.sync_api import expect
from pages.login_page import LoginPage
from features.variables import BASE_URL, USERNAME, PASSWORD

@given("the user is on the login page")
def login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.goto(BASE_URL)
    expect(context.page).to_have_title(LoginPage.TITLE)

@when("the user enter username and password")
def enter_login_detail(context):
    context.login_page.login(USERNAME, PASSWORD)

@then('the user land on the dashboard page')
def verify_dashboard(context):
    expect(context.page.locator(LoginPage.PRODUCT_PAGE)).to_be_visible()

@when("the user enter the {username} and {password}")
def enter_login_detail_with_params(context, username, password):
    context.login_page.login(username, password)

@then("the {error_message} is displayed")
def verify_error_message(context, error_message):
    error_display = context.page.locator(context.login_page.ERROR_MSG_ELEMENT)
    expect(error_display).to_have_text(error_message)