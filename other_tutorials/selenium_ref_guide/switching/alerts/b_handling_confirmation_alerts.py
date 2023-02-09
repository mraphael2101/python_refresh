import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Alerts in web applications are helpful in getting user attention or seek information before proceeding with some action

Alerts take the focus away from the current window and force the browser to read the message.
Alert prevents the user from accessing other parts of the web page until the box is closed.

Selenium WebDriver can handle three types of alerts:

Simple Alert: A simple alert displays a message and an OK button. It's used to display a message to the user.
Confirmation Alert: A confirmation alert displays a message and two buttons, OK and Cancel. It's used to confirm the user's choice.
Prompt Alert: A prompt alert displays a message and a textbox for the user to enter a value. It's used to get user input.

Note: Windows alerts(example: Authentication popup seeking Admin Credentials while accessing any Network drive)
handling is out of box of Selenium Capabilities, we need to depend on third party Tools like AutoIT
"""

driver = webdriver.Chrome
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, 'button#confirmButton').click()
time.sleep(3)
ale = driver.switch_to.alert
time.sleep(3)
print(ale.text)
# dismissing alert
ale.dismiss()
time.sleep(3)
print(driver.find_element(By.CSS_SELECTOR, 'span#confirmResult').text)
time.sleep(3)
driver.quit()
