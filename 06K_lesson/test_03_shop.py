import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_03_form(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    driver.maximize_window()
# Авторизация
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
        "standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
        "secret_sauce")

    driver.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()
# Добавление в корзину
    driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-backpack"]').click()

    driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-onesie"]').click()
# Перейти в корзину
    driver.find_element(By.CSS_SELECTOR,
                        'a[class="shopping_cart_link"]').click()
# Кнопка checkout
    driver.find_element(By.CSS_SELECTOR, 'button[id="checkout"]').click()
# Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Анна")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петрова")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
# Кнопка continue
    driver.find_element(By.CSS_SELECTOR, 'input[id="continue"]').click()
# Текст со страницы
    txt_total_label = driver.find_element(
        By.CSS_SELECTOR, "div[data-test='total-label']").text
# Закрытие браузера
    driver.quit()
# Сравнение
    assert txt_total_label == "Total: $58.29"
    print(txt_total_label)
