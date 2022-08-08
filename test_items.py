import time


from selenium.webdriver.common.by import By


def test_lang(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    time.sleep(2) # пауза чтобы увидеть язык сайта
