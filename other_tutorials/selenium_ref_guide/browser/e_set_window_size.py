import time

from selenium import webdriver

"""
# set_window_size():

# driver.set_window_size(width,height) resizes the window based on width and height passed in params,
# height and width are measured in pixels
# This method is helpful in testing responsive browsers
# example: driver.set_window_size(400, 600)
width and height
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.set_window_size(400, 600)
time.sleep(5)
driver.set_window_size(2400, 3200)
time.sleep(10)
driver.quit()
