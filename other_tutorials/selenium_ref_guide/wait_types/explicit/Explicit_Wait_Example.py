from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
- An Explicit wait will finish evaluation after the specified timeout condition elapses

- A standard set of wait conditions is available for web testing from the
  Selenium Library. An example of one is presence_of_element_located()
"""


class ExplicitWaitDemo:

    def __init__(self, dri_obj, seconds=1):
        self.driver = dri_obj
        self.secs = seconds
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def demo_explicit_wait(self):
        wait = WebDriverWait(self.driver, self.secs)
        wait.until(EC.presence_of_element_located((By.ID, "MADEUP_INVALID")))

    # Here we are handling the exception as shown in previous classes
    def entry_point(self):
        try:
            self.demo_explicit_wait()
        except TimeoutException:
            print("TimeoutException was raised after " + str(self.secs) + " seconds")


driver = webdriver.Chrome()
demo = ExplicitWaitDemo(driver, 10)
demo.entry_point()
