import time

from selenium import webdriver

"""
set_window_rect method not only resizes the browser window but also can set the position of the browser window by providing the x and y coordinate
example: driver.set_window_rect(100, 100, 400, 600)
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.set_window_rect(100, 100, 400, 600)
time.sleep(5)
driver.set_window_rect(300, 500, 400, 600)
time.sleep(5)
driver.quit()