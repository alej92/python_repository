from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    print(f"Нажатие {i + 1}/5")

delete = len(driver.find_elements(
    By.CSS_SELECTOR, 'button.added-manually'))

print(f"Длина списка: {delete}")
