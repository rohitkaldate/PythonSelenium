import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Courses").click()
time.sleep(2)
#Mouse actions using the following class
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.LINK_TEXT,"More ")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"About us")).click().perform()
