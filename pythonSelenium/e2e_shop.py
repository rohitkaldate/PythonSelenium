import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pythonSelenium.locators import dropdown

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"Shop").click()
webelements = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for element in webelements:
    product = element.find_element(By.XPATH,"div/h4/a").text
    if product == "Blackberry":
        element.find_element(By.XPATH,"div/button").click()
        break

driver.find_element(By.CSS_SELECTOR,"a[class$='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
wait= WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
result= driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
print(result)
assert "Success" in result
