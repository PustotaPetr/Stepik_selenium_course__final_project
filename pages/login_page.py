from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') >= 0, \
            "Current URL doesn`t contain substr 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIRST_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    
