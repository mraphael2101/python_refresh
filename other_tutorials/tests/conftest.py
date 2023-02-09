import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    """
    - An example of a hook that allows you to pass an option from the commandline
    - Utilise by typing:  pytest -s tests/test_e2e.py --browser_name=chrome
    """
    parser.addoption("--browser_name", action="store", default="edge")


# def pytest_generate_tests(metafunc):
#     # This is called for every test. Only get/set command line arguments
#     # if the argument is specified in the list of test "fixturenames".
#     option_value = metafunc.config.option.name
#     if 'name' in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("browser_name", [option_value])


@pytest.fixture(scope="class")
def lifecycle_management(request):
    global driver
    browser_pref = request.config.getoption("browser_name")

    if browser_pref == "chrome":
        driver = webdriver.Chrome()
    elif browser_pref == "edge":
        driver = webdriver.Edge()

    request.cls.driver = driver

    yield

    driver.quit()
