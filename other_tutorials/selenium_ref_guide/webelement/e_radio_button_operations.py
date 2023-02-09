import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
Radio Button element in webpage will have input tag and type attribute is Radio
To select radio button we can either click on required checkbox or respective label

--> checkbox and radio buttons can be selected using .click() method 
--> .selected() method helps in finding required radio button is selected or not

# Select the radio button
radio_button.click()

# Check if the radio button is selected
if radio_button.is_selected():
    print("Radio button is selected")
else:
    print("Radio button is not selected")

"""
edgeservice = Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
driver.refresh()
time.sleep(5)

yesRadioLabel = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yesRadio = driver.find_element(By.XPATH, "//input[@id='yesRadio']")
print("initial yes radio button selected status is: "+str(yesRadio.is_selected()))

# selecting radio button
yesRadioLabel.click()
time.sleep(5)
print("Yes radio button selected status is: "+str(yesRadio.is_selected()))
driver.quit()


