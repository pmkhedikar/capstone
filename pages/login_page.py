class LoginPage:
    # Locators
    TITLE = "Swag Labs"
    USERNAME = "id=user-name"
    PASSWORD = "id=password"
    LOGIN_BUTTON = "id=login-button"
    PRODUCT_PAGE = "xpath=//span[text()='Products']"
    ERROR_MSG_ELEMENT = "//h3[@data-test='error']"

    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def is_on_login_page(self):
        return self.page.title() == self.TITLE

    def login(self, username, password):
        self.page.locator(self.USERNAME).fill(username)
        self.page.fill(self.PASSWORD, password)
        self.page.locator(self.LOGIN_BUTTON).click()

    def is_on_dashboard(self):
        return self.page.locator(self.PRODUCT_PAGE).is_visible()

    def get_error_message(self):
        return self.page.locator(self.ERROR_MSG_ELEMENT).inner_text()