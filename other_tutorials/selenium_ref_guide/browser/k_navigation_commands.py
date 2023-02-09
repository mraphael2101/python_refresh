import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""
Navigation commands are some which enable the user to navigate through the history of the browser
 like back,forth, refresh.
Basically, these navigation commands are nothing but the browser navigation buttons,
We can use these commands only when these buttons are enabled.

back() method navigates the user back to the last page
forward() helps the user to navigate forward when already is moved back
refresh() helps the user to refresh current browser
Different ways of refreshing webpage
1.driver.get(driver.current_url)
2. driver.find_element(By.TAG_NAME,"body").send_keys(Keys.F5)
3. driver.refresh()
4. driver.find_element_by_tag_name("body").send_keys("\uE035")

"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.get("https://yahoo.com")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.refresh()
time.sleep(5)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.F5)
time.sleep(5)
driver.quit()
