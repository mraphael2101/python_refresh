import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Functions:
    """
    - Returns the Selenium element if found
    """

    def __init__(self, dri_obj):
        self.driver = dri_obj
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def __call__(self, dri_obj):
        return dri_obj.find_element(By.XPATH, "//input[@type='search']")


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
ele = wait.until(Functions(driver))
ele.send_keys("Carrots")
time.sleep(3)
