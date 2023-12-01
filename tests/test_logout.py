from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_login_and_logout(browser):
    login_link = 'http://34.141.58.52:8080/#/login'

    login_page = LoginPage(browser, login_link)
    logout_page = LogoutPage(browser, login_link)

    login_page.open()

    login_page.go_to_login()
    login_page.go_to_password()
    login_page.go_to_button()

    logout_page.go_to_logout()

    browser.save_screenshot('result_logout.png')
