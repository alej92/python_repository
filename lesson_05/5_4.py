from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

driver.find_element(By.XPATH, '//p[text()="Close"]').click()
sleep(5)

driver.quit()
