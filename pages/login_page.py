from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_input.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REPEAT)
        password_field2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

    def should_be_login_url(self):
        assert ("login" in self.url), f"Expected 'login' to be substring of {self.url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form"
