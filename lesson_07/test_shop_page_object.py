import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.shop import Shop

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_shop(driver):
    shop = Shop(driver)
    shop.login("standard_user")
    shop.password("secret_sauce")
    shop.input()
    shop.tovar1()
    shop.tovar2()
    shop.tovar3()
    shop.korzina()
    shop.knopka_checkout()
    shop.first_name("Анна")
    shop.last_name("Петрова")
    shop.postal_code("123456")
    shop.knopka_continue()
    text = shop.text()
    assert text == "Total: $58.29"
