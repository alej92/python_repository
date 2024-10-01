from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("https://uitestingplayground.com/classattr")
clickable = driver.find_element(
        By.CSS_SELECTOR, "button.btn-primary").click()

sleep(8)