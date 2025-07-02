class AddToCartPage:
    PRODUCT_LIST = "xpath=//*[@class='inventory_item_name ' and text()='{PRODUCT_NAME}']"
    ADD_TO_CART =(
        "(//*[text()='{PRODUCT_NAME}']//following::div//button[text()='Add to cart'])[1]"
    )
    REMOVE_FROM_CART = (
        "(//*[text()='{PRODUCT_NAME}']//following::div//button[text()='Remove'])[1]"
    )
    CART = "xpath=//span[@data-test='shopping-cart-badge']"

    def __init__(self, page):
        self.page = page

    def select_product(self, product_name):
        locator = self.PRODUCT_LIST.format(PRODUCT_NAME=product_name)
        return self.page.locator(locator).is_visible()

    def add_to_cart(self, product_name):
        locator = self.ADD_TO_CART.format(PRODUCT_NAME=product_name)
        self.page.locator(locator).click()

    def remove_from_cart(self, product_name):
        locator = self.REMOVE_FROM_CART.format(PRODUCT_NAME=product_name)
        self.page.locator(locator).click()

    def get_cart_count(self):
        return self.page.locator(self.CART).inner_text()