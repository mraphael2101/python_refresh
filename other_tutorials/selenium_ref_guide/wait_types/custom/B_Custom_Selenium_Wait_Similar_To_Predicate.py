from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Predicates:
    """
    - An expectation for checking that an element has a particular class as an attribute
    - The locator is used to find the element
    - Returns True if the class attribute is identified otherwise raises a TimeoutException
    """

    def __init__(self, dri_obj, locator, class_name):
        self.driver = dri_obj
        self.locator = locator
        self.class_val = class_name
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def __call__(self, dri_obj):
        element = dri_obj.find_element(*self.locator)  # Finding the referenced element
        if self.class_val in element.get_attribute("class"):
            return True


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
outcome = wait.until(Predicates(driver, (By.XPATH, "//div[@class='products']"), "products"))
print(outcome)
outcome = wait.until(Predicates(driver, (By.XPATH, "//div[@class='products']"), "doesnotexist"))
print(outcome)
