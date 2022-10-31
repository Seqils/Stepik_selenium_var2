from .base_page import BasePage
from .locators import ProductPageLocators

PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


class ProductPage(BasePage):

    def click_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_right_order(self):
        self.should_be_same_name()
        self.should_be_same_price()

    def should_be_same_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_ALERT).text, "Names not the same"

    def should_be_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == \
               self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text, "Prices not the same"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success massage is presented, " \
                                                                          "but should not be"
