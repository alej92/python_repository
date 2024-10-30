from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()


    def time(self, time):
        self._driver.find_element(By.CSS_SELECTOR, "input[id='delay']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[id='delay']").send_keys(
        time)
        
    def seven(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()

    def plus(self):
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()

    def eight(self):
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()

    def equals(self):
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result_test(self):
        test = WebDriverWait(self._driver, 46, 0.1)
        test.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ('div[class="screen"]')), "15")
        )
        result_test = self._driver.find_element(By.CSS_SELECTOR, ('div[class="screen"]')).text
        assert result_test == "15"
