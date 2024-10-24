from selenium.webdriver.common.by import By

class Shop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()


    def login(self, login):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
        login)

    def password(self, password):
        self._driver.find_element(By.CSS_SELECTOR, "#password").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
        password)

    def input(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

    def tovar1(self):
        self._driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-backpack"]').click()

    def tovar2(self):
        self._driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    def tovar3(self):
        self._driver.find_element(By.CSS_SELECTOR,
                        'button[id="add-to-cart-sauce-labs-onesie"]').click()
        
    def korzina(self):
        self._driver.find_element(By.CSS_SELECTOR,
                        'a[class="shopping_cart_link"]').click()
        
    def knopka_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[id="checkout"]').click()

    def first_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(name)

    def last_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(name)

    def postal_code(self, code):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)

    def knopka_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="continue"]').click()

    def text(self):
        text = self._driver.find_element(By.CSS_SELECTOR, 
                                    "div[data-test='total-label']").text
        return text
    