import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

## Handle the checkboxes dynamically.
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

## Handles the radio buttons dynamically
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))

for button in radiobuttons:
    if button.get_attribute('value') == "radio2":
        button.click()
        assert button.is_selected()
        break

driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()



time.sleep(2)