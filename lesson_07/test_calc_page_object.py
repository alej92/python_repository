import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.calc import Calculator

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calc(driver):
    calc = Calculator(driver)
    calc.time("45")
    calc.seven()
    calc.plus()
    calc.eight()
    calc.equals()
    calc.result_test()
