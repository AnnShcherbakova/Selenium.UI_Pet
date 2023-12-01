import time
from pages.edit_pet_profile_page import PetEditProfilePage
from tests.test_login_page import test_go_to_login


def test_go_to_edit_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = PetEditProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_profile()
    time.sleep(2)
    page.go_to_edit_pet_name()
    time.sleep(2)
    page.go_to_edit_pet_age()
    time.sleep(2)
    page.go_to_edit_pet_type()
    page.go_to_edit_choose_pet_type_cat()
    page.go_to_edit_choose_pet_gender()
    page.go_to_edit_choose_pet_gender_female()

    image_path = r'images/3.jpg'
    page.go_to_edit_photo_pet_button(image_path)

    time.sleep(2)
    page.go_to_edit_photo_pet_button_second()
    page.go_to_save_pet_button()
    browser.save_screenshot('result_edit_profile_pet.png')
