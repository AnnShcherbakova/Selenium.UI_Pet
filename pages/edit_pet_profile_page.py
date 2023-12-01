import os
import time
import pyautogui
from .base_page import BasePage
from .locators import PetEditProfileLocators


class PetEditProfilePage(BasePage):

    def go_to_edit_pet_profile(self):
        edit_pet_profile_button = self.browser.find_element(*PetEditProfileLocators.EDIT_PROFILE_BTN)
        edit_pet_profile_button.click()

    def go_to_edit_pet_name(self):
        add_pet_name = self.browser.find_element(*PetEditProfileLocators.EDIT_PET_NAME)
        add_pet_name.clear()
        add_pet_name.send_keys('Mary')

    def go_to_edit_pet_age(self):
        add_pet_age = self.browser.find_element(*PetEditProfileLocators.EDIT_PET_AGE)
        add_pet_age.clear()
        add_pet_age.send_keys('7')

    def go_to_edit_pet_type(self):
        edit_choose_pet_type = self.browser.find_element(*PetEditProfileLocators.EDIT_CHOOSE_PET_TYPE)
        edit_choose_pet_type.click()

    def go_to_edit_choose_pet_type_cat(self):
        edit_choose_pet_type_cat = self.browser.find_element(*PetEditProfileLocators.EDIT_CHOOSE_PET_TYPE_CAT)
        edit_choose_pet_type_cat.click()

    def go_to_edit_choose_pet_gender(self):
        edit_choose_pet_gender = self.browser.find_element(*PetEditProfileLocators.EDIT_CHOOSE_PET_GENDER)
        edit_choose_pet_gender.click()

    def go_to_edit_choose_pet_gender_female(self):
        edit_choose_pet_gender_female = self.browser.find_element(*PetEditProfileLocators.EDIT_CHOOSE_PET_GENDER_FEMALE)
        edit_choose_pet_gender_female.click()

    def go_to_edit_photo_pet_button(self, file_path):
        edit_photo_pet_button = self.browser.find_element(*PetEditProfileLocators.EDIT_CHOOSE_PHOTO_BTN)
        edit_photo_pet_button.click()

        time.sleep(2)

        image_path = os.path.abspath(file_path)

        pyautogui.write(image_path)
        pyautogui.press('enter')

        time.sleep(5)

    def go_to_edit_photo_pet_button_second(self):
        go_to_edit_photo_pet_button = self.browser.find_element(*PetEditProfileLocators.SECOND_EDIT_PHOTO_BTN)
        go_to_edit_photo_pet_button.click()
        time.sleep(2)

    def go_to_save_pet_button(self):
        save_pet_button = self.browser.find_element(*PetEditProfileLocators.SAVE_ADD_PET_BTN)
        save_pet_button.click()
