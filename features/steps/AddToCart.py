from behave import given,when,then
from playwright.sync_api import expect
from pages.add_to_cart_page import AddToCartPage

@when("user selects the item form product list")
def add_to_cart(context):
    if context.page.locator(AddToCartPage.PRODUCT_LIST.format(PRODUCT_NAME='Sauce Labs Backpack')).is_visible():
        context.page.locator(AddToCartPage.ADD_TO_CART.format(PRODUCT_NAME='Sauce Labs Backpack')).click()

@then("the item is added to the cart")
def verify_cart(context):
    context.page.wait_for_timeout(5000)
    expect(context.page.locator(AddToCartPage.CART)).to_contain_text('1')


