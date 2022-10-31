import time
import pytest

from .pages.product_page import ProductPage


# @pytest.mark.parametrize('number', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                                   # "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                   # pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  #  "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{number}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_order()
