"""
if usefixture is mentioned at class level all the methods, fixture will be applied to all methods in class
@pytest.mark.usefixtures("fixture name")

"""
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestExample:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @pytest.fixture(params=["https://demoqa.com/", "https://google.com/"])
    def multiple_urls(self, request):
        return request.param

    def test_example1(self, driver):
        driver.get("https://google.com/")
        driver.maximize_window()
        print(driver.title)
        assert driver.title == "Google"

    def test_example2(self, driver):
        driver.get("https://demoqa.com/")
        driver.maximize_window()
        print(driver.title)
        assert driver.title == "DEMOQA"

    def test_example3(self, driver,multiple_urls):
        driver.get(multiple_urls)
        driver.maximize_window()
        print(driver.title)
