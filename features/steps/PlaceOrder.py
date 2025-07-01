from behave import given,when,then
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

@when("the user complete the checkout")
def WhenTheUserComplete(context):
    if expect(context.page.get_by_text(PlaceOrderPage.CHECKOUT_BUTTON)).is_visible():
        context.page.get_by_text(PlaceOrderPage.CHECKOUT_BUTTON).click()

@when("order is confirmed")
def order_confirmed(context):
    context.page.get_by_placeholder(PlaceOrderPage.FNAME).fill("Parag")
    context.page.get_by_placeholder(PlaceOrderPage.LNAME).fill("Khedikar")
    context.page.get_by_placeholder(PlaceOrderPage.ZIP).fill("411045")
    context.page.locator(PlaceOrderPage.CONTINUE_BUTTON).click()

@then("order placed successfully")
def order_placed(context):
    if expect(context.page.get_by_text(PlaceOrderPage.FINISH_BUTTON)).is_visible():
        context.page.get_by_text(PlaceOrderPage.FINISH_BUTTON).click()

    expect(context.page.get_by_text(PlaceOrderPage.ORDER_PLACED_MSG)).to_be_visible()






