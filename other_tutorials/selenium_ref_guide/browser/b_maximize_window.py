import time

from selenium import webdriver

"""
Maximizes the browser  Syntax: driver.maximize_window()
Best practice is to maximize browser before performing any action/validation
if browser is already maximized and if you call maximize_window() method, it will not have any effect on browser
"""
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.quit()
