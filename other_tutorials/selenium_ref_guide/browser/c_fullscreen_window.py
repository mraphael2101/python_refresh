
import time

from selenium import webdriver

"""
Set the browser size to full screen  Syntax: driver.fullscreen_window()
When browser is in full screen we will be not able to see title bar, addressbar, URL bar and windows taskbar
You will be able to see only webpage, similar to pressing fn+f11 manually
"""
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.fullscreen_window()
time.sleep(10)
driver.quit()
