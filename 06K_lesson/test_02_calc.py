import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_02_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
# Ввести значение 45
    time = driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
    time.clear()
    time.send_keys("45")
# 7+8=
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
# Проверить, что в окне отобразится результат 15 через 45 секунд
    test = WebDriverWait(driver, 46, 0.1)
    test.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ('div[class="screen"]')), "15")
        )
    result_test = driver.find_element(By.CSS_SELECTOR, ('div[class="screen"]')).text
    assert result_test == "15"
    print(result_test)
    driver.quit()
