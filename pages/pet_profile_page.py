import os
import time
import pyautogui
from .base_page import BasePage
from .locators import PetProfileLocators


class PetProfilePage(BasePage):

    def go_to_create_pet_profile(self):
        create_pet_profile_button = self.browser.find_element(*PetProfileLocators.CREATE_PROFILE_BTN)
        create_pet_profile_button.click()

    def go_to_add_pet_name(self):
        add_pet_name = self.browser.find_element(*PetProfileLocators.ADD_PET_NAME)
        add_pet_name.send_keys('Nik')

    def go_to_add_pet_age(self):
        add_pet_age = self.browser.find_element(*PetProfileLocators.ADD_PET_AGE)
        add_pet_age.send_keys('4')

    def go_to_choose_pet_type(self):
        choose_pet_type = self.browser.find_element(*PetProfileLocators.CHOOSE_PET_TYPE)
        choose_pet_type.click()

    def go_to_choose_pet_type_dog(self):
        choose_pet_type_dog = self.browser.find_element(*PetProfileLocators.CHOOSE_PET_TYPE_DOG)
        choose_pet_type_dog.click()

    def go_to_choose_pet_gender(self):
        choose_pet_gender = self.browser.find_element(*PetProfileLocators.CHOOSE_PET_GENDER)
        choose_pet_gender.click()

    def go_to_choose_pet_gender_male(self):
        choose_pet_gender_male = self.browser.find_element(*PetProfileLocators.CHOOSE_PET_GENDER_MALE)
        choose_pet_gender_male.click()

    def go_to_submit_add_pet_button(self):
        submit_add_pet_button = self.browser.find_element(*PetProfileLocators.SUBMIT_ADD_PET_BTN)
        submit_add_pet_button.click()

    def go_to_choose_photo_add_pet_button(self, file_path):
        choose_photo_add_pet_button = self.browser.find_element(*PetProfileLocators.CHOOSE_PHOTO_BTN)
        choose_photo_add_pet_button.click()

        time.sleep(2)

        image_path = os.path.abspath(file_path)

        pyautogui.write(image_path)
        pyautogui.press('enter')

        time.sleep(5)

    def go_to_choose_photo_add_pet_button_second(self):
        choose_photo_add_pet_button = self.browser.find_element(*PetProfileLocators.CHOOSE_PHOTO_BTN)
        choose_photo_add_pet_button.click()
        time.sleep(2)

    def delete_pet_profile(self):
        delete_button = self.browser.find_element(*PetProfileLocators.DELETE_PROFILE_BTN)
        delete_button.click()

    def delete_pet_profile_second(self):
        delete_button_yes = self.browser.find_element(*PetProfileLocators.DELETE_PROFILE_BTN_YES)
        delete_button_yes.click()
