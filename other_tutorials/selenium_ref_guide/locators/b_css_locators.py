"""
CSS selectors are  more concise and easy-to-read syntax to select elements based on their tag name, class, and attributes.
Here's a summary of CSS selector examples that can be used to locate elements on a web page:

Syntax: "tagname[attribute='attributevalue']"
To locate all elements with a specific class:"tagname[class='calssvalue']" shortcut:  ".calssvalue"
To locate all elements with a specific ID: "tagname[id='idvalue']"  shortcut:   "#idvalue"
To locate all elements with a specific tag: "tag"
To locate all elements with a specific attribute, regardless of its value: "[attribute]"
To locate all elements with a specific attribute and value: "[attribute='value']"
To locate elements that are child of a specific element ( Direct child): "parent > *"
To locate elements that are following immediate sibling of a specific element: "element + *"
To locate elements that are following sibling of a specific element: "element ~ *
To locate the nth element of a specific tag: "tag:nth-of-type(n)"
To locate elements that contain a specific text: "*:contains('text')"    [ Note: Prefer to choose Xpath contains method]
To locate elements that match a certain pattern: "tag[attribute*='pattern']"
To locate elements that begins with pattern :  [attribute^=’pattern’]
To locate elements that ends with pattern :  [attribute$=’pattern’]
To locate elements that contains pattern :  [attribute*=’pattern’]
To locate an element based on its position within its parent: "parent > :nth-child(n)"  example:  [ div button:nth-child(2):
    Locates the second child of a div element, which is a button element ]
To locate all elements that are the last child of their parent: "parent > :last-child"
To locate all elements that are the first child of their parent: "parent > :first-child"
To locate elements that are the first or last child of their parent: "parent > :first-child, parent > :last-child"
To locate elements that have a specific class and also a specific attribute: "tag.class[attribute='value']"
To locate elements that are descendant of a specific element: "ancestor descendant"
"""

import time

from selenium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

edgeservice=Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[id='userName']").send_keys("Murali D")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='name@example.com']").send_keys("murali.d@bt.com")
driver.find_element(By.CSS_SELECTOR,"textarea#currentAddress").send_keys("B3 1DB")
driver.find_element(By.CSS_SELECTOR,"textarea#permanentAddress").send_keys("Bangalore")
driver.find_element(By.CSS_SELECTOR,"button.btn-primary").click()
time.sleep(5)
driver.quit()






