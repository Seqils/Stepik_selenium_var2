import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage, PRODUCT_PAGE_LINK
import time


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "12345"
        self.link = PRODUCT_PAGE_LINK
        page = ProductPage(browser, self.link)
        page.open()
        browser.implicitly_wait(10)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email=email, password=password)

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_authorized_user()
        page.click_add_to_basket()
        page.should_be_right_order()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_be_right_order()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_of_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
