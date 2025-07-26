import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform() ##move to the element or the mouseover
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()