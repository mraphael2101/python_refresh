from selenium.webdriver.common.by import By

"""
Rather than mixing the code that models the page structure with the raw selenium 
code we are separating them which makes the code more readable and maintainable
"""


class HomePage:

    def __init__(self, driver):
        # You should be able to distinguish between an instance variable and a statio/class variable by now
        self.driver = driver

    __name_txtfield = (By.XPATH, "//div[@class='form-group//input[@name='name']")  # static class variable

    __gender_ddl = (By.ID, "exampleFormControlSelect1")

    __shop_link = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_name_txtfield(self):
        """
        asterix is provided to treat the variable/locator as a tuple as it is surrounded by ()
        it needs to be deserialized
        """
        return self.driver.find_element(*HomePage.__name_txtfield)

    def get_gender_ddl(self):
        return self.driver.find_element(*HomePage.__gender_ddl)

    def go_to_shop(self):
        return self.driver.find_element(*HomePage.__shop_link)
