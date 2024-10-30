import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.form import Form

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form(driver):
    form = Form(driver)
    form.name("Иван")
    form.surname("Петров")
    form.address("Ленина, 55-3")
    form.email("test@skypro.com")
    form.phone_number("+7985899998787")
    form.zip_code("")
    form.city("Москва")
    form.country("Россия")
    form.job_position("QA")
    form.company("SkyPro")
    form.knopka_submit()
    form.danger_color()
    form.success_color()
