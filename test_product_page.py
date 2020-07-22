from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
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


product_pages = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"]


@pytest.mark.parametrize('link', list_of_urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_is_right()
    page.product_price_is_right()
    time.sleep(2)


@pytest.mark.parametrize('product_page', product_pages)
@pytest.mark.skip(reason="ORIGINALLY BROKEN")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, product_page):
    page = ProductPage(browser, product_page)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('product_page', product_pages)
def test_guest_cant_see_success_message(browser, product_page):
    page = ProductPage(browser, product_page)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Originally xfailed")
@pytest.mark.parametrize('product_page', product_pages)
def test_message_disappeared_after_adding_product_to_basket(browser, product_page):
    page = ProductPage(browser, product_page)
    page.open()
    page.add_product_to_basket()
    page.message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_has_not_items()
    basket_page.basket_is_empty()
