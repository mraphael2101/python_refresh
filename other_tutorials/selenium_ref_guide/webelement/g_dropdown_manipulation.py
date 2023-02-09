import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""
-->Dropdown are formed using select tag in html,
-->if dropdown is not formed with select tag you cannot use this Select Class methods

Below Methods Present in Select Class can be used to perform operations on Dropdown
select_by_index(int index)
select_by_value(String value)
select_by_visible_text(String text)
options()
first_selected_option()
all_selected_options()
deselect_by_index(int index)
deselect_by_value(String value)
deselect_by_visible_text(String text)
deselect_all()


--> For Non select class Dropdowns we should rely on custom user defined methods

"""
driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.refresh()
time.sleep(5)
dropdown = Select(driver.find_element(By.ID, 'oldSelectMenu'))

# select by index
dropdown.select_by_index(4)
# time.sleep(5)
print("option selected is " + dropdown.first_selected_option.text)

dropdown.select_by_value("red")
print("option selected is " + dropdown.first_selected_option.text)
# time.sleep(5)

dropdown.select_by_visible_text("Yellow")
print("option selected is " + dropdown.first_selected_option.text)
# time.sleep(5)


cars_dropdown = Select(driver.find_element(By.ID, "cars"))
cars_dropdown.select_by_index(2)
# time.sleep(5)

print("option selected in carsDropDown is " + cars_dropdown.first_selected_option.text)

# time.sleep(5)
cars_dropdown.select_by_value("audi")

print("option selected in carsDropDown is " )
options_selected = cars_dropdown.all_selected_options
for option in options_selected:
    print(option.text)

# time.sleep(5)
cars_dropdown.select_by_visible_text("Saab")
print("option selected in carsDropDown is ")

options_selected = cars_dropdown.all_selected_options
for option in options_selected:
    print(option.text)

# Get all options
options = cars_dropdown.options
for option in options:
    print(option.text)

driver.quit()
