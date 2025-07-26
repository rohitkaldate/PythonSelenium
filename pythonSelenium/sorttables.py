import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

veggies = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
elements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in elements:
    veggies.append(ele.text)
print(veggies)
original_veggies = veggies.copy()
veggies.sort()
print(original_veggies)

assert original_veggies == veggies

 