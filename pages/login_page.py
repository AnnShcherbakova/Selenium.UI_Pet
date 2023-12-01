import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('mypet@gmail.com')

    def go_to_password(self):
        password_email = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        password_email.send_keys("987654321pet")

    def go_to_button(self):
        button_email = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        button_email.submit()
        time.sleep(5)
