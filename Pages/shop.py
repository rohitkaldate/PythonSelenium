from selenium.webdriver.common.by import By

class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_link = (By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']")

    def shopItems(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        webelements = self.driver.find_elements(*self.product_cards)

        for element in webelements:
            product = element.find_element(By.XPATH, "div/h4/a").text
            if product == "product_name":
                element.find_element(By.XPATH, "div/button").click()
                break

    def checkout(self):
        self.driver.find_element(*self.checkout_link).click()