from pages.main_page import MainPage


def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result5.png')

def test_go_to_main_page_and_filter_dog(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_dog_filter()
    browser.save_screenshot('result_dog_filter.png')

def test_go_to_main_page_and_filter_cat(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_cat_filter()
    browser.save_screenshot('result_cat_filter.png')

def test_go_to_main_page_and_filter_reptile(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_reptile_filter()
    browser.save_screenshot('result_reptile_filter.png')

def test_go_to_main_page_and_filter_humster(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.select_humster_filter()
    browser.save_screenshot('result_hamster_filter.png')

def test_go_to_main_page_and_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name("Tosha")
    browser.save_screenshot('result_name_filter.png')
