import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
An iframe (inline frame) is a HTML document embedded within another HTML document on a website. 
When you work with iframes in Selenium Webdriver, you need to switch from the main page to the iframe and perform actions in it.
and then switch back to the main page.
Here's how to handle iframes in Selenium Webdriver using Python:

-->Locate the iframe: Before you can interact with the iframe, you need to locate it on the page. 
    You can do this using various methods like find_element_by_tag_name, find_element_by_id, find_element_by_name, etc.
-->Switch to the iframe: Once you have located the iframe, you can switch to it using the switch_to.frame method. 
    You can pass the index of the iframe, its name, or its WebElement to the switch_to.frame method.
--> Perform actions in the iframe: Once you have switched to the iframe, 
    you can perform various actions like clicking elements, entering text, etc.
--> Switch back to the main page: After you have performed the actions in the iframe, 
you need to switch back to the main page to perform further actions. You can do this using the switch_to.default_content method.


"""

driver = webdriver.Chrome()
driver.get("https://chercher.tech/practice/frames")
driver.maximize_window()
driver.implicitly_wait(20)
print(driver.find_element(By.CSS_SELECTOR,"h1.breadcrumb-item").text)

# Switch to frame using ID
driver.switch_to.frame("frame1")
driver.find_element(By.CSS_SELECTOR, "b#topic+input").send_keys("Murali")
# Switch to inner frame using ID
driver.switch_to.frame("frame3")
driver.find_element(By.CSS_SELECTOR, "input#a").click()
time.sleep(5)

print("select checkbox in inner frame ")

# Switch to default frame
driver.switch_to.default_content()

driver.switch_to.frame("frame2")
animals = Select(driver.find_element(By.ID, "animals"))
animals.select_by_value("babycat")

time.sleep(5)
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h1.breadcrumb-item").text)
driver.quit()
