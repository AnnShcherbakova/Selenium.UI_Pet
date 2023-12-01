
from .base_page import BasePage
from .locators import LogoutPageLocators


class LogoutPage(BasePage):
    def go_to_logout(self):
        logout_link = self.browser.find_element(*LogoutPageLocators.LOGOUT_LINK)
        logout_link.click()




