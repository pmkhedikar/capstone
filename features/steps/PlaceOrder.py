from behave import given, when, then
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.place_order_page import PlaceOrderPage
from pages.add_to_cart_page import AddToCartPage
from features.steps.login import login, enter_login_detail
from features.steps.AddToCart import add_to_cart, verify_cart

@given("user logged in and has item in cart")
def LoginAndAdditem(context):
    login(context)
    enter_login_detail(context)
    add_to_cart(context)
    verify_cart(context)
    context.page.locator(AddToCartPage.CART).click()
    context.place_order_page = PlaceOrderPage(context.page)

@when("the user complete the checkout")
def WhenTheUserComplete(context):
    context.place_order_page.click_checkout()

@when("order is confirmed")
def order_confirmed(context):
    context.place_order_page.fill_customer_details("Parag", "Khedikar", "411045")
    context.place_order_page.click_continue()

@then("order placed successfully")
def order_placed(context):
    context.place_order_page.click_finish()
    expect(context.page.get_by_text(PlaceOrderPage.ORDER_PLACED_MSG)).to_be_visible()