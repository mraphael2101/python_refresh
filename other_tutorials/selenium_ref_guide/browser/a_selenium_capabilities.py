import time

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    driver.refresh()
    time.sleep(5)
    print("Title : " + driver.title)
    print("URL : " + driver.current_url)
    print("Page source : " + driver.page_source)
    driver.get_screenshot_as_file("test.png")
    driver.find_element(By.XPATH, "").is_displayed()
    driver.find_elements(By.XPATH).count()
    driver.find_elements(By.XPATH).__getattribute__("name")
    driver.quit()
