import time

from selenium import webdriver

"""
get_window_size():

Gets the width and height of the current window
Syntax: driver.get_window_size()

get_window_position():
Gets the x,y position of the current window
Syntax: driver.get_window_position()


get_window_rect():

Gets the x, y coordinates of the window as well as height and width of the current window.
Syntax: driver.get_window_rect()

"""
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)

print("window size is")
print(driver.get_window_size())
print("window position is")
print(driver.get_window_position())
print("window rect is")
print(driver.get_window_rect())
driver.maximize_window()
print("window size is")
print(driver.get_window_size())
print("window position is")
print(driver.get_window_position())
print("window rect is")
print(driver.get_window_rect())

time.sleep(5)
driver.quit()
