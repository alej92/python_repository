from selenium.webdriver.common.by import By

class Form:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.maximize_window()


    def name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(
        name)
        
    def surname(self, surname):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(
        surname)

    def address(self, address):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(
        address)

    def email(self, email):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(
        email)

    def phone_number(self, number):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(
        number)

    def zip_code(self, code):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(
        code)

    def city(self, city):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(
        city)

    def country(self, country):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(
        country)

    def job_position(self, job_position):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(
        job_position) 
    
    def company(self, company):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").clear()
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(
        company)
         
    def knopka_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    def danger_color(self):
        alert_danger_color = "rgba(248, 215, 218, 1)"
        color_zip = self._driver.find_element(By.ID, "zip-code").value_of_css_property(
        "background-color")
        assert color_zip == alert_danger_color


    def success_color(self):
        alert_success_color = "rgba(209, 231, 221, 1)"
        fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", 
              "country", "job-position", "company"]
        for field in fields:
            color_field = self._driver.find_element(By.ID, field).value_of_css_property(
            "background-color")
            assert color_field == alert_success_color


