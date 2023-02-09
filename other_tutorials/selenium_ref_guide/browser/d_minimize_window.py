
import time

from selenium import webdriver

# minimizes the browser

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
time.sleep(5)
driver.minimize_window()
time.sleep(5)
print(driver.title)
driver.quit()
