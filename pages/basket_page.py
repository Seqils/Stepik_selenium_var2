from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
            "There is at least one item, should be none"

    def should_be_message_of_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "There is none message of empty basket"

    def should_be_an_item_in_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_ITEMS), \
            "There are no items in basket, should be at least one"
