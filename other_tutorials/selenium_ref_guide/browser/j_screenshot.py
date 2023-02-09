import base64
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""

1.get_screenshot_as_file() method is used to take a screenshot and save it to a file. 
get_screenshot_as_base64() method is used to take a screenshot and 
return it as a base64 encoded string which can be saved as a file. 
It will be helpful to embed screenshot in html report
2.save_screenshot() method is used to take a screenshot and save it to a file.
 we can also capture screenshot of specific element
3.get_screenshot_as_file() will raise an exception if the file cannot be saved.
 On the other hand, save_screenshot() will return False, but it will not raise an exception.

"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.save_screenshot("savescreenshot.png")
time.sleep(5)
driver.get_screenshot_as_file("getscreenshot.png")
time.sleep(5)
screenshot = driver.get_screenshot_as_base64()# Decode the base64 encoded string and save it to a file
print(screenshot)
with open("screenshot.png", "wb") as f:
    f.write(base64.decodebytes(screenshot.encode('utf-8')))
driver.find_element(By.ID, "windowButton").screenshot("webelement.png")
time.sleep(5)
driver.quit()
