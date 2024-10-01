from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/entry_ad")
clickable = driver.find_element(
        By.CSS_SELECTOR, "div.modal-footer").click()

sleep(8)