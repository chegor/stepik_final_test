from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage(BasePage):

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def product_name_is_right(self):
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED)
        page_h1 = self.browser.find_element(*ProductPageLocators.PAGE_H1)
        #print(added_product.text)
        #print(page_h1.text)
        assert page_h1.text == added_product.text, "WRONG PRODUCT ADDED"

    def product_price_is_right(self):
        added_product_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE)
        page_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        #print(added_product_price.text)
        #print(page_price.text)
        assert added_product_price.text == page_price.text, "WRONG PRICE ADDED in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappear"