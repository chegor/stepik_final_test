from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    PAGE_H1 = (By.CSS_SELECTOR, "h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")