import time

from selenium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
We usually work with elements like text box, button, menus, sub-menus, radio button, headers, footer, links, plain texts, forms so on.
click() method is used to click buttons, checkbox, radio buttons and links
sendKeys() method sets text into an editable element (text bar, text area, button) without replacing the previously available content.
clear() method will help the user to clear the field on the webpage, if we do not clear a field then also selenium will not throw any exception, but it just appends the new value with the old value.
submit() method in selenium submits a form. Users can use it only along with form or with form elements only. 
submit() method clicks a button is a misconception; it works only when that particular button is associated with the form
get_attribute() method fetches required attribute value example: driver.find_element_by_id("q").get_attribute("title")
get_attibute() method fetches the value of an attribute
print("Title of google searchbar : "+ driver.find_element_by_id("q").get_attribute("title"))
getAttibute() returns blank as a value if the attribute is not set to any value
getAttibute() returns 'null' if there no such attribute

"""

edgeservice=Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/text-box")
driver.fullscreen_window()
time.sleep(5)
driver.find_element(By.ID, "userName").send_keys("Murali D")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='name@example.com']").send_keys("murali.d@bt.com")
driver.find_element(By.CSS_SELECTOR, "textarea#currentAddress").send_keys("B3 1DB")
driver.find_element(By.CSS_SELECTOR, "textarea#permanentAddress").send_keys("Bangalore\nBirmingham")
class_attribute = driver.find_element(By.CSS_SELECTOR, "button.btn-primary").get_attribute("class")
print("class attribute value of submit button is " + class_attribute)
# driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").submit()
time.sleep(5)
driver.quit()
