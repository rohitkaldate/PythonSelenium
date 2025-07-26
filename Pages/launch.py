class Launch:
    def __init__(self, driver):
        self.driver = driver

    def launchPage(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        print(self.driver.title)
        print(self.driver.current_url)