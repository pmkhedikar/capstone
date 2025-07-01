from behave import given,when,then
from playwright.sync_api import expect
from pages.login_page import LoginPage
from features.variables import BASE_URL,USERNAME,PASSWORD


@given("user logged in with valid credentials")
@given("the user is on the login page")
def login(context):
    context.page.goto(BASE_URL)
    expect(context.page).to_have_title(LoginPage.TITLE)


@when("the user enter username and password")
def enter_login_detail(context):
    context.page.locator(LoginPage.USERNAME).fill(USERNAME)
    context.page.fill(LoginPage.PASSWORD, PASSWORD)
    context.page.locator(LoginPage.LOGIN_BUTTON).click()

@then('the user land on the dashboard page')
def verify_dashboard(context):
    expect(context.page.locator(LoginPage.PRODUCT_PAGE)).to_be_visible()


@when("the user enter the {username} and {password}")
def enter_login_detail(context, username, password):
    context.page.locator(LoginPage.USERNAME).fill(username)
    context.page.fill(LoginPage.PASSWORD, password)
    context.page.locator(LoginPage.LOGIN_BUTTON).click()


@then("the {error_message} is displayed")
def verify_error_message(context,error_message):
    expect(context.page.locator(LoginPage.ERROR_MSG_ELEMENT)).to_contain_text(error_message)

