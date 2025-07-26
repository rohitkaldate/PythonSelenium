from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Purchase:
    def __init__(self, driver):
        self.driver = driver
        self.final_checkout = (By.XPATH, "//button[@class='btn btn-success']")
        self.address = (By.CSS_SELECTOR, "#country")
        self.country_name = (By.LINK_TEXT, "India")
        self.checkbox_link = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.final_purchase = (By.XPATH, "//input[@value='Purchase']")
        self.validate = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def purchase_product(self):
        self.driver.find_element(*self.final_checkout).click()

    def delivery_address(self, countryName):
        self.driver.find_element(*self.address).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(self.country_name))
        self.driver.find_element(*self.country_name).click()
        self.driver.find_element(*self.checkbox_link).click()
        self.driver.find_element(*self.final_purchase).click()

    def validate_result(self):
        result = self.driver.find_element(*self.validate).text
        assert "Success" in result