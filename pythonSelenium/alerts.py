import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID,"name").send_keys("Rohit")
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert  #---used to handle the alert or the popups
text_verify = alert.text
print(text_verify)

assert "Rohit" in text_verify
alert.accept()


time.sleep(2)