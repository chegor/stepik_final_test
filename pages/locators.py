from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_1_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_2_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    PAGE_H1 = (By.CSS_SELECTOR, "h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "form.basket_summary basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "div#content_inner")