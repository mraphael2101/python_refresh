from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    __country_txtfield = (By.ID, "country")

    __country_optlst = (By.XPATH, "//div[@class='suggestions']/ul/li/a/text()")

    __agree_terms_chkbox = (By.XPATH, "//label[@for='checkbox2']")

    __purchase_btn = (By.XPATH, "//input[@value='Purchase']")

    def get_country_txtfield(self):
        return self.driver.find_element(*ConfirmationPage.__country_txtfield)

    def get_agree_terms_chkbox(self):
        return self.driver.find_element(*ConfirmationPage.__agree_terms_chkbox)

    def get_purchase_btn(self):
        return self.driver.find_element(*ConfirmationPage.__purchase_btn)

    def select_country_opt_from_list(self, val):
        loc_string = "//div[@class='suggestions']/ul/li/a[contains(text(),'{}')]".format(val)
        self.driver.find_element(By.XPATH, loc_string).click()
