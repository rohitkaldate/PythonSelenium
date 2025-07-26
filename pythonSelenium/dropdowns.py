import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
time.sleep(2)

## This is handling for the dynamic dropdowns
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value") == "India"