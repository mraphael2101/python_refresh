from selenium.webdriver.common.by import By

from other_tutorials.page_objects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    __product_container_list = (By.XPATH, "//div[@class='card h-100']")

    __product_name_list = (By.XPATH, "//div[@class='card h-100']/div/h4/a")

    __product_container_btn = (By.XPATH, "//div[@class='card h-100']/div[2]/button")

    __go_to_cart_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    __checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def get_product_containers(self):
        return self.driver.find_elements(*CheckoutPage.__product_container_list)

    def get_product_names(self):
        return self.driver.find_elements(*CheckoutPage.__product_name_list)

    def get_product_container_btn(self):
        return self.driver.find_elements(*CheckoutPage.__product_container_btn)

    def get_go_to_cart_btn(self):
        return self.driver.find_element(*CheckoutPage.__go_to_cart_btn)

    def get_checkout_btn(self):
        return self.driver.find_element(*CheckoutPage.__checkout_btn)

    def get_checkout_page_object(self):
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page
