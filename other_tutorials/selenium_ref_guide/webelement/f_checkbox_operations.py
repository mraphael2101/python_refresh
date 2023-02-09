import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
Checkbox element in webpage will have input tag and type attribute is checkbox
To select checkbox we can either click on required checkbox or respective label

--> checkbox and radio buttons can be selected using .click() method 
--> .selected() method helps in finding required checkbox is selected or not

# Select the checkbox
checkbox.click()

# Check if the checkbox is selected
if checkbox.is_selected():
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")
    
# Deselect the checkbox (if selected)
if checkbox.is_selected():
    checkbox.click()

"""
edgeservice = Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.refresh()
time.sleep(5)
checkboxLabel = driver.find_element(By.XPATH, "//input[@id='tree-node-home']/..")
checkbox = driver.find_element(By.XPATH, "//input[@id='tree-node-home']")

print("initial checkbox status is: "+str(checkbox.is_selected()))

# selecting checkbox if not selected
if not checkbox.is_selected():
    checkboxLabel.click()
time.sleep(5)
print("After selecting checkbox, status is: "+str(checkbox.is_selected()))

# unselecting checkbox if  selected
if checkbox.is_selected():
    checkboxLabel.click()
time.sleep(5)
print("After deselecting checkbox, status is: "+str(checkbox.is_selected()))

driver.quit()


