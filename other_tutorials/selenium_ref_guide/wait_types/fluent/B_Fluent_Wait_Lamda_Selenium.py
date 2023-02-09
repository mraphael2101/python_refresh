from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Example:

    def __init__(self, dri_obj, seconds, poll_frequency):
        self.driver = dri_obj
        self.secs = seconds
        self.poll_freq = poll_frequency
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def fluent_wait_with_lambda_selenium(self, lamda_expr):
        WebDriverWait(self.driver, self.secs, self.poll_freq).until(lamda_expr)
        print("The element was displayed")


driver = webdriver.Chrome()
obj_ref = Example(driver, 5, 0.1)
obj_ref.fluent_wait_with_lambda_selenium(lambda d: d.find_element(By.XPATH, "//div[@class='products']").is_displayed())

