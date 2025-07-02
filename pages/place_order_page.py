class PlaceOrderPage:
    CHECKOUT_BUTTON = "Checkout"
    FNAME = "First Name"
    LNAME = "Last Name"
    ZIP = "Zip/Postal Code"
    CONTINUE_BUTTON = "id=continue"
    FINISH_BUTTON = "Finish"
    ORDER_PLACED_MSG = "Thank you for your order!"

    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        self.page.get_by_text(self.CHECKOUT_BUTTON).click()

    def fill_customer_details(self, fname, lname, zip_code):
        self.page.get_by_placeholder(self.FNAME).fill(fname)
        self.page.get_by_placeholder(self.LNAME).fill(lname)
        self.page.get_by_placeholder(self.ZIP).fill(zip_code)

    def click_continue(self):
        self.page.locator(self.CONTINUE_BUTTON).click()

    def click_finish(self):
        self.page.get_by_text(self.FINISH_BUTTON).click()

    def is_order_placed(self):
        return self.page.get_by_text(self.ORDER_PLACED_MSG).is_visible()