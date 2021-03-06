from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Current page is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not displayed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not displayed"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)
        input_email = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_email.send_keys(password)
        input_email = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input_email.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()


