import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
--> Handling multiple tabs  in Selenium WebDriver is similar to handling multiple windows 

1) Store the current window handle: 
2) Get a list of all window handles:
3) Switch to the new window: 
4) Perform actions on the new window: 
5) Close the new window: 
6) Switch back to the original window: 
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.implicitly_wait(20)

# Store the current window handle
parent_window_handle = driver.current_window_handle

driver.find_element(By.CSS_SELECTOR, 'button#tabButton').click()
time.sleep(5)

# Get all the window handles
window_handles = driver.window_handles

# Loop through the window handles

for handle in window_handles:
    # Switch to the new window
    if handle != parent_window_handle:
        driver.switch_to.window(handle)
        break
# perform action on new window
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.ID, 'sampleHeading').text)
driver.close()
time.sleep(5)
driver.switch_to.window(parent_window_handle)
driver.quit()
