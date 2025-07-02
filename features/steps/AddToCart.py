from behave import given,when, then
from playwright.sync_api import expect
from pages.add_to_cart_page import AddToCartPage
from pages.login_page import LoginPage
from features.variables import BASE_URL, USERNAME, PASSWORD


PRODUCT_NAME = 'Sauce Labs Backpack'

@given("user logged in with valid credentials")
def login_with_cred(context):
    context.login_page = LoginPage(context.page)
    context.login_page.goto(BASE_URL)
    expect(context.page).to_have_title(LoginPage.TITLE)
    context.login_page.login(USERNAME, PASSWORD)


@when("user selects the item form product list")
def add_to_cart(context):
    context.cart_page = AddToCartPage(context.page)
    if context.cart_page.select_product(PRODUCT_NAME):
        context.cart_page.add_to_cart(PRODUCT_NAME)

@then("the item is added to the cart")
def verify_cart(context):
    cart_element = context.page.locator(context.cart_page.CART)
    expect(cart_element).to_have_text('1')