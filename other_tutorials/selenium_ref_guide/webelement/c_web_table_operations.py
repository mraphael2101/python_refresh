import time

from selenium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

"""
--> Standard webtables will be have in <table> </table> tag, however in angualr and react applications we will not have tables with <table> tag,
    in that case we need to identify table, table header, table rows and columns based on attributes inside div tag
--> In Selenium Python, you can perform various operations on a web table, such as finding table size, reading data, searching for data,
     and manipulating data. 
--> Here's a detailed explanation of the common tasks that you can perform on tables in Selenium Python:

# Locate the table element table = driver.find_element_by_xpath("//table[@id='example']") 
# Get all rows of the table rows = table.find_elements_by_xpath(".//tr") 
# Get the number of rows num_rows = len(rows) 
# Get the number of columns in the first row (assuming all rows have the same number of columns)
num_columns = len(columns) 
# Print the size of the table print("Table size: {} rows x {} columns".format(num_rows, num_columns))

"""

edgeservice = Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
driver.refresh()
time.sleep(5)



table = driver.find_element(By.XPATH, "//div[@class='rt-table']")
# //finding number of cells in header
columns = driver.find_elements(By.XPATH, "//div[@role='row'][1]//div[@role='columnheader']")
rows = driver.find_elements(By.XPATH, "//div[@class='rt-tbody']//div[@role='row']")
print("Table size: {} rows x {} columns".format(len(rows), len(columns)))


# get number of rows excluding header
noOfRowsExcludingHeader = len(rows)
# get number of columns
noOfColumns = len(columns)
allData = []
# iterate over the rows, to ignore the headers we have started the i with '1'
for i in range(1, noOfRowsExcludingHeader):
    # reset the row data every time
    ro = []
    # iterate over columns
    for j in range(1, noOfColumns):
        # get text from the i th row and j th column
        ro.append(driver.find_element(By.XPATH, "(//div[@class='rt-tbody']//div[@role='row'])[" + str(i) + "]//div[@role='gridcell'][" + str(j) + "]").text)
    # add the row data to allData of the self.table
    allData.append(ro)
print(allData)

# fetch required cell data
rowNumber = 3
columnNumber = 3
cellData = table.find_element(By.XPATH, "(//div[@class='rt-tbody']//div[@role='row'])[" + str(rowNumber) + "]//div[@role='gridcell'][" + str(columnNumber) + "]").text
print("cell text at row : "+str(rowNumber) + " and column  " + str(columnNumber) + " is " + cellData)
driver.quit()
