import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter your email address']").send_keys("demo@gmail.com")#--->Relative XPath
driver.find_element(By.XPATH,"//div/form/div[2]/input").send_keys("Hello@1234")#---->Absolute XPath
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Hello@1234")#--->CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(4) button").click()

time.sleep(2)