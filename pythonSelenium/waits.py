import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

## Add products to cart
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']`").send_keys("rahulshettyacademy")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(5)

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

