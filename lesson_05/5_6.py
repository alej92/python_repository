from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME, "button").click()

driver.quit()
