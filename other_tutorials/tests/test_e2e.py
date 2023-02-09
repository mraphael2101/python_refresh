import time

from other_tutorials.page_objects.CheckoutPage import CheckoutPage
from other_tutorials.page_objects.HomePage import HomePage
from other_tutorials.tests.BaseClass import BaseClass


class TestRegressionSuite1(BaseClass):

    def test_e2e(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice")
        home_page = HomePage(self.driver)
        time.sleep(2)
        home_page.go_to_shop().click()
        time.sleep(2)

        checkout_page = CheckoutPage(self.driver)
        product_name_list = checkout_page.get_product_names()
        counter = 0
        actual_product_list = []
        for product_name in product_name_list:
            print(product_name.text)
            actual_product_list.append(product_name.text)
            # Add Blackberry item to the cart only
            if product_name.text == "Blackberry":
                checkout_page.get_product_container_btn()[counter].click()
                print("Clicked on Blackberry")
            counter += 1
        assert "Blackberry" in actual_product_list

        checkout_page.get_go_to_cart_btn().click()
        checkout_page.get_checkout_btn().click()

        confirmation_page = checkout_page.get_checkout_page_object()
        confirmation_page.get_country_txtfield().send_keys("united k")
        self.verify_link_presence("United Kingdom")
        time.sleep(2)

        confirmation_page.select_country_opt_from_list("Kingdom")
        time.sleep(2)
        confirmation_page.get_agree_terms_chkbox().click()
        confirmation_page.get_purchase_btn().click()
        time.sleep(2)
