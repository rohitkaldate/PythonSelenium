import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.LINK_TEXT,"Click Here").click()
##Switch to new window tab
window = driver.window_handles
driver.switch_to.window(window[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()
driver.switch_to.window(window[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

