from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    LIKE_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) >'
                                    ' div > div > div > div:nth-of-type(3) > '
                                    'div:nth-of-type(2) > span > i')

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class FilterLocators:
    FILTER_DROPDOWN = (By.XPATH, '//*[@id="pv_id_2"]/div[1]/span[1]')
    DOG_OPTION = (By.CSS_SELECTOR, "#pv_id_2_0")
    CAT_OPTION = (By.CSS_SELECTOR, "#pv_id_2_1")
    REPTILE_OPTION = (By.CSS_SELECTOR, "#pv_id_2_2")
    HAMSTER_OPTION = (By.CSS_SELECTOR, "#pv_id_2_3")


class FilterByNameLocators:
    NAME_FILTER_INPUT = (By.CSS_SELECTOR, "input#petName")


class PetProfileLocators:
    CREATE_PROFILE_BTN = (By.CSS_SELECTOR, "#app > main > div > div > div > div > div > button")
    ADD_PET_NAME = (By.ID, 'name')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_DOG = (By.XPATH, '//*[@aria-label="dog"]')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    SUBMIT_ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CHOOSE_PHOTO_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')
    CHOOSE_PHOTO_BTN_SECOND = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')
    DELETE_PROFILE_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div:nth-of-type(2) > div > div:nth-of-type(5) > '
                                           'div > div:nth-of-type(2) > button:nth-of-type(2)')
    DELETE_PROFILE_BTN_YES = (By.CSS_SELECTOR, "html > body > div:nth-of-type(3) > div:nth-of-type(2) > "
                                               "button:nth-of-type(2)")

class LogoutPageLocators:
    LOGOUT_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-of-type(2) > a')


class PetEditProfileLocators:
    EDIT_PROFILE_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div:nth-of-type(2) > '
                                         'div > div > div > div:nth-of-type(2) > button')
    EDIT_PET_NAME = (By.ID, 'name')

    EDIT_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    EDIT_CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    EDIT_CHOOSE_PET_TYPE_CAT = (By.XPATH, '//*[@aria-label="hamster"]')

    EDIT_CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    EDIT_CHOOSE_PET_GENDER_FEMALE = (By.XPATH, '//*[@aria-label="Female"]')
    EDIT_CHOOSE_PHOTO_BTN = (By.CSS_SELECTOR, '#app > main > div > form > '
                                              'div > div:nth-of-type(2) > div:nth-of-type(2) '
                                              '> div > div:nth-of-type(2)'
                                              ' > div > div:nth-of-type(2) > div > span')
    SECOND_EDIT_PHOTO_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/form[1]/div[1]/div[2]'
                                       '/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]')
    SAVE_ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/form[1]/div[1]'
                                  '/div[2]/div[3]/button[1]/span[2]')
