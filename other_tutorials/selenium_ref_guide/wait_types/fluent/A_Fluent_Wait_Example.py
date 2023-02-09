from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
- A Fluent wait is a type of Explicit wait that is capable of ignoring
  certain types of Exceptions until a given time condition elapses
  
- It is also possible to specify a polling frequency to determine when 
  to check the condition
  
- A standard set of wait conditions is available for web testing from the
  Selenium Library. An example of one is presence_of_element_located()
"""


class FluentWaitDemo:
    ignored_exceptions = [TimeoutException, NoSuchElementException]
    poll_frequency = 0.1  # the default value is 0.5 milliseconds

    def __init__(self, dri_obj, seconds=1):
        self.my_wait = WebDriverWait(dri_obj, seconds)
        self.driver = dri_obj
        self.secs = seconds
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def demo_fluent_wait(self):
        # Example 1
        WebDriverWait(driver, self.secs, self.poll_frequency, ignored_exceptions=self.ignored_exceptions) \
            .until(EC.presence_of_element_located((By.XPATH, "//div[@class='products']")))
        print("element //div[@class='products'] was present in the DOM")

    def demo_ele_not_found_exc(self):
        elex = self.driver.find_element(By.ID, "FICTITIOUS")
        elex.click()

    # We are handling the exceptions here
    def entry_point(self):
        try:
            trigger_exception_list = [self.demo_fluent_wait(), self.demo_ele_not_found_exc()]
            for method in trigger_exception_list:
                pass
        except TimeoutException:
            print("TimeoutException was raised after " + str(self.secs) + " seconds")
        except NoSuchElementException:
            print("NoSuchElementException was raised for element ID FICTITIOUS")


# Examine the program's behaviour by modifying the number of seconds. Try 0 and 5
driver = webdriver.Chrome()
demo = FluentWaitDemo(driver, 5)
demo.entry_point()
