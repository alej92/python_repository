from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

locator = "input"
input = driver.find_element(By.CSS_SELECTOR, locator)
input.send_keys("1000")
sleep(2)
input.clear()
sleep(2)
input.send_keys("999")
sleep(2)