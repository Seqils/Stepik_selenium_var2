from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, "div.row h1")
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "[id='messages'] > div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[id='messages'] > div:nth-child(1)")
    # price locator p.price_color
    # basket price locator div.alertinner p strong
    # name of the book div.row h1
    # [id="messages"] > div:nth-child(1) strong
