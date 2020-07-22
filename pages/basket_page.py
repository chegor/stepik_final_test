from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_has_not_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "BASKET has items, but it should not"

    def basket_is_empty(self):
        text_basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        assert "Your basket is empty." in text_basket_empty.text, "Basket is not empty, bit it should be"
