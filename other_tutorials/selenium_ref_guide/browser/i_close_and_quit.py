import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Close the browser:
driver.close() method closes current browser
syntax: driver.close()
quit browser:

driver.quit() method closes all the windows opened by instance

"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, "windowButton").click()
time.sleep(5)
# driver.close()
# time.sleep(5)
driver.quit()
time.sleep(5)
