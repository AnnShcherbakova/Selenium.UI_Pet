import time
from pages.pet_profile_page import PetProfilePage
from tests.test_login_page import test_go_to_login


def test_go_to_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = PetProfilePage(browser, link)
    page.open()
    page.go_to_create_pet_profile()
    page.go_to_add_pet_name()
    page.go_to_add_pet_age()
    page.go_to_choose_pet_type()
    page.go_to_choose_pet_type_dog()
    page.go_to_choose_pet_gender()
    page.go_to_choose_pet_gender_male()
    page.go_to_submit_add_pet_button()

    image_path = r'images/22.jpg'

    page.go_to_choose_photo_add_pet_button(image_path)

    time.sleep(2)
    page.go_to_choose_photo_add_pet_button_second()
    browser.save_screenshot('result_create_profile_pet.png')

    page.delete_pet_profile()
    time.sleep(2)
    page.delete_pet_profile_second()
    browser.save_screenshot('result_delete_profile_pet.png')
