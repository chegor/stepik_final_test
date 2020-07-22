from .base_page import BasePage
from .locators import LoginPageLocators

import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form"


    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL_INPUT)
        email_field.send_keys(email)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", email_field)
        pass1_field = self.browser.find_element(*LoginPageLocators.REG_FORM_1_PASS)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.REG_FORM_2_PASS)
        pass2_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_FORM_SUBMIT_BUTTON)
        button.click()
