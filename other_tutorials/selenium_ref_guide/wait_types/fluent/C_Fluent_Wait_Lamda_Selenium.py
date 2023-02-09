from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Example:

    def __init__(self, dri_obj, seconds, poll_frequency):
        self.driver = dri_obj
        self.secs = seconds
        self.poll_freq = poll_frequency
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def handler(self, lamda_expr):
        WebDriverWait(self.driver, self.secs, self.poll_freq).until(lamda_expr)
        print("The element was displayed")

    def entry_point(self):
        try:
            obj.handler(lambda d: len(d.find_elements(By.XPATH, "//div[@class='product']/h4")) > 10)
            obj.handler(lambda d: len(d.find_elements(By.XPATH, "madeup_invalid")) > 10)  # Raises TimeoutException
        except TimeoutException:
            print("TimeoutException was raised after " + str(self.secs) + " seconds")


driver = webdriver.Chrome()
obj = Example(driver, 5, 0.1)
obj.entry_point()
