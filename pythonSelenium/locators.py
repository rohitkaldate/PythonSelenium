import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME,"name").send_keys("Rohit")#----> locator name
driver.find_element(By.NAME,"email").send_keys("kaldaterohit9@gmail.com")#--->locator name
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")#--->Locator ID
driver.find_element(By.ID,"exampleCheck1").click()#--->Locator ID
driver.find_element(By.ID, "inlineRadio2").click()#--->Locator ID
driver.find_element(By.NAME,"bday").send_keys("26-11-2000")#--->locator name
driver.find_element(By.XPATH,"//input[@value='Submit']").click()#--->locator XPATH
text=driver.find_element(By.CLASS_NAME,"alert").text#--->locator CLASS_NAME
print(text)

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello Rohit")#--->locator XPATH
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()#--->locator XPATH
assert "Success" in text#--->Assertion or Validation

## Handle the static Dropdown---> It is present inside the select tag and handled using the Select Class as follows:
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")

time.sleep(1)
