import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
is_enabled(), is_displayed(), and is_selected() are methods provided by Selenium WebDriver to check the state of elements on a webpage.
                Here are some examples and explanations of how to use these methods:

is_enabled() - This method is used to check whether a given element is enabled or not. 
                An enabled element can be interacted with, for example, a text field can be filled with text and a button can be clicked.

is_displayed() is a method provided by Selenium WebDriver to check whether a given element is visible on the page or not. 
                However, if the element is not present in the DOM, it will raise a NoSuchElementException.

is_selected() - This method is used to check whether a given element is selected or not. 
                This method is helpful to check radio button/checkbox is selected

"""
edgeservice = Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()
driver.refresh()

enableAfter = driver.find_element(By.ID, "enableAfter")
print("enable after button enabled ?: " +  str(enableAfter.is_enabled()))
try:
    # Locate the element using XPath
    element = driver.find_element(By.ID, "visibleAfter")
    # Check if the element is displayed on the page
    if element.is_displayed():
        print("visibleAfter button Element is displayed")
    else:
        print("visibleAfter button is not displayed")
except NoSuchElementException:
    print("visibleAfter Element not found")

time.sleep(5)

enableAfter = driver.find_element(By.ID, "enableAfter")
print("enable after button enabled ?: " +  str(enableAfter.is_enabled()))
try:
    # Locate the element using XPath
    element = driver.find_element(By.ID, "visibleAfter")
    # Check if the element is displayed on the page
    if element.is_displayed():
        print("visibleAfter button Element is displayed")
    else:
        print("visibleAfter button is not displayed")
except NoSuchElementException:
    print("visibleAfter Element not found")

driver.quit()


