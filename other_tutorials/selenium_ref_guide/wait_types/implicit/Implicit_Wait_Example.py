import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("print immediately")
time.sleep(5)
print("printed after 5 seconds")


"""
- An implicit wait tells WebDriver to poll the DOM for a certain amount of time
  when trying to find any element. This can be useful when certain elements are 
  not immediately available and need some time to load

- once set, the implicit wait is set for the life of the session

- Do not mix implicit wait_types with explicit wait_types as this may cause unpredictable
  wait times e.g. setting an implicit wait of 10 seconds and an explicit wait 
  for 15 seconds could cause a timeout to occur after 20 seconds
"""

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")
