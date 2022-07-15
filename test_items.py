import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def test_items(self, browser, page):
    link = "http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button is not None, "Элемент не найден"