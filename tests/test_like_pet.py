from pages.main_page import MainPage

def test_like_pet(browser):
    main_page_link = 'http://34.141.58.52:8080/#/'
    main_page = MainPage(browser, main_page_link)
    main_page.open()
    main_page.like_pet()

    browser.save_screenshot('result_like_pet.png')

