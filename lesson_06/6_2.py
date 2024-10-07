from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")
text = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
text.clear()
text.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)
driver.quit()
