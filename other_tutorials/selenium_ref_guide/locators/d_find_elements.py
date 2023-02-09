import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
findElements: A command to identify a list of web elements within the web page
Returns a list of multiple matching web elements
Returns an empty list if no matching element is found
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")
driver.maximize_window()
time.sleep(5)
linksList = driver.find_elements(By.CSS_SELECTOR, "div#linkWrapper a")
print(len(linksList))
for ele in linksList:
    print(ele.text)
driver.quit()
