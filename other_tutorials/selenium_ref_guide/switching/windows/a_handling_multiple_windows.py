import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
--> Handling multiple windows in Selenium WebDriver can be a bit tricky, especially when you don't know how many windows are going to be opened 
    and what actions you need to perform on each window. Here are some steps to handle multiple windows in Selenium:

1) Store the current window handle: 
2) Get a list of all window handles: 
3) Switch to the new window: 
4) Perform actions on the new window:
5) Close the new window: 
6) Switch back to the original window: 
--> It's important to note that you need to switch back to the original window before you close the new window, 
    otherwise, you may end up closing the original window as well. Also, you should always make sure to switch back to the original window 
    after you have finished performing actions on the new window, otherwise, you may end up performing actions on the wrong window.
"""

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
driver.implicitly_wait(20)

# Store the current window handle
parent_window_handle = driver.current_window_handle

driver.find_element(By.CSS_SELECTOR, 'button#windowButton').click()
time.sleep(5)

# Get all the window handles
window_handles = driver.window_handles

# Loop through the window handles

for handle in window_handles:
    # Switch to the new window
    time.sleep(2)
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
