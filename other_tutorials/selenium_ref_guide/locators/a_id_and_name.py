
"""
Different Type of locators

In Selenium WebDriver locators are used to locate web elements on a webpage so that Selenium can interact with them.

Selenium WebDriver offers several types of locators that can be used to locate elements on a web page.
Some of the most commonly used locators are:

--> ID: The ID attribute of an element is used to locate the element. Syntax: driver.find_element(By.ID,"id_value")
--> Name: The name attribute of an element is used to locate the element. Syntax: driver.find_element(By.NAME,"namevalue")
--> Class Name: The class attribute of an element is used to locate the element. Syntax: driver.find_element(By.CLASS_NAME,"classnamevalue")
--> Tag Name: The tag name of an element is used to locate the element. Syntax: driver.find_element(By.TAG_NAME,"tagnamevalue")
--> Link Text: The link text of a link element is used to locate the element. Syntax: driver.find_element(By.LINK_TEXT,"linktextvalue")
--> Partial Link Text: A part of the link text of a link element is used to locate the element. Syntax: driver.find_element(By.PARTIAL_LINK_TEXT,"partiallinktextvalue")
--> CSS Selector: The CSS selector of an element is used to locate the element. Syntax: driver.find_element(By.CSS_SELECTOR,"cssselectorvalue")
--> XPath: The XPath of an element is used to locate the element. Syntax: driver.find_element(By.XPATH,"xpathvalue")
"""


import time

from selenium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

edgeservice=Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/text-box")
driver.find_element(By.ID, "userName").send_keys("murali")
driver.find_element(By.TAG_NAME, "button").click()
driver.find_elements()
time.sleep(5)
driver.quit()