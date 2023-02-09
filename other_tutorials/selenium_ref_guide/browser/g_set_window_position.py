import time

from selenium import webdriver

"""
set_window_position:
sets the coordinates of browser starting point, top left corner is considered as (0,0) position
Syntax: driver.set_window_position(300, 300)
Args:
 - x: the x-coordinate in pixels to set the window position
 - y: the y-coordinate in pixels to set the window position
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.set_window_position(300, 300)
time.sleep(5)
driver.set_window_position(100, 100)
time.sleep(5)
driver.quit()
