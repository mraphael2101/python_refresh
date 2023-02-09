
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

edgeservice = Service(executable_path="C:\\drivers\\msedgedriver.exe")
driver = webdriver.Edge(service=edgeservice)
driver.get("https://www.bt.com/")
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(5)
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='TrustArc Cookie Consent Manager']"))
driver.switch_to.frame(0)
driver.find_element(By.XPATH, "//a[contains(text(),'Accept all cookies')]").click()
time.sleep(5)
driver.quit()
