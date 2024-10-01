from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")


username = driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")
clickable = driver.find_element(
        By.CSS_SELECTOR, "button.radius").click()

sleep(4)
