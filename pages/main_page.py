from selenium.webdriver import Keys
from .locators import MainPageLocators, FilterLocators, FilterByNameLocators
from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def select_dog_filter(self):
        filter_dropdown = self.browser.find_element(*FilterLocators.FILTER_DROPDOWN)
        filter_dropdown.click()

        dog_option = self.browser.find_element(*FilterLocators.DOG_OPTION)
        dog_option.click()

    def select_cat_filter(self):
        filter_dropdown = self.browser.find_element(*FilterLocators.FILTER_DROPDOWN)
        filter_dropdown.click()

        dog_option = self.browser.find_element(*FilterLocators.CAT_OPTION)
        dog_option.click()

    def select_reptile_filter(self):
        filter_dropdown = self.browser.find_element(*FilterLocators.FILTER_DROPDOWN)
        filter_dropdown.click()

        dog_option = self.browser.find_element(*FilterLocators.REPTILE_OPTION)
        dog_option.click()

    def select_humster_filter(self):
        filter_dropdown = self.browser.find_element(*FilterLocators.FILTER_DROPDOWN)
        filter_dropdown.click()

        dog_option = self.browser.find_element(*FilterLocators.HAMSTER_OPTION)
        dog_option.click()

    def filter_by_name(self, name):
        name_filter_input = self.browser.find_element(*FilterByNameLocators.NAME_FILTER_INPUT)
        name_filter_input.send_keys(name)
        name_filter_input.send_keys(Keys.ENTER)

    def like_pet(self):
        like_button = self.browser.find_element(*MainPageLocators.LIKE_BUTTON)
        like_button.click()
