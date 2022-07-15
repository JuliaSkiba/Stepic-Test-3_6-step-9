from selenium.webdriver.common.by import By
import time


class Test_Button_Exists:
    def test_button(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(10)
        browser.implicitly_wait(5)
        button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button is not None, "Элемент не найден"
