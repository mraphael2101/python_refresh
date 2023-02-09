"""
To locate all elements: "//*"
To locate all elements with a specific attribute, regardless of its value: "//*[@attribute]"
To locate all elements with a specific attribute and value: "//*[@attribute='value']"
To locate the nth element of a specific tag: "(//tag)[n]"
To locate elements that contain a specific text: "//*[contains(text(), 'text')]"
To locate elements that match a certain pattern: "//*[matches(text(), 'pattern')]"
To locate elements that have multiple attributes and values: "//*[@attribute1='value1' and @attribute2='value2']"=
To locate elements that have one of multiple attributes and values: "//*[@attribute1='value1' or @attribute2='value2']"
To locate an element based on its position within its parent: "(//parent/*)[n]"
To locate elements that are descendant of a specific element: "//ancestor//descendant"
To locate elements that are child of a specific element: "//parent/*"
To locate elements that are preceding sibling of a specific element: "//preceding-sibling::*"
To locate elements that are following sibling of a specific element: "//following-sibling::*"
To locate elements that have a specific class and also a specific attribute: "//*[contains(@class,'className') and @attribute='value']"
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
driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Murali D")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("murali.d@bt.com")
driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']").send_keys("B3 1DB")
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Bangalore")
driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
time.sleep(5)
driver.quit()
