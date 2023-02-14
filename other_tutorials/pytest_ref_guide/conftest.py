import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup():
    print("create driver instance")
    print("launch browser")
    yield
    print("close  browser")


@pytest.fixture(scope='class')
def setup():
    print("**********")
    print("setup executed")
    yield
    print("**********")
    print("teardown executed")


@pytest.fixture()
def userdata():
    return ["Murali", "Mark"]


@pytest.fixture(params=["murali", "Mark"])
def multiple_sets_data(request):
    return request.param


@pytest.fixture
def driver1():
    service = Service(executable_path="/Users/domda1/Documents/drivers/msedgedriver")
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


@pytest.fixture(params=["https://demoqa.com/", "https://google.com/"])
def multiple_sets_data(request):
    return request.param


# @pytest.fixture
# def setup():
#     driver = webdriver.Edge()
#     yield
#     driver.quit()
