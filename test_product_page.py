from .pages.product_page import ProductPage
import pytest
import time

list_of_urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason = "bug in last commit")),
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.parametrize('link', list_of_urls )
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_is_right()
    page.product_price_is_right()
    time.sleep(1)


