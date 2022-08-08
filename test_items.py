import time
from selenium.webdriver.common.by import By


def test_add_item_to_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(10)
    browser.get(link)

    # чтобы по заданию корректно отработал assert пришлось получать массив кнопок по селектору и сравнивать с 0
    assert len(browser.find_elements(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')) != 0, "Кнопка добавления товара в корзину отсутствует"
    # browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket') # <- вполне рабочий вариант

    time.sleep(5) # пауза чтобы увидеть язык сайта
    # не стал ставить 30 секунд как по заданию, ибо можно уснуть в ожидании, а иначе процессы вебдрайвера не завершатся