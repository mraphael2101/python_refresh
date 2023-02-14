"""
if usefixture is mentioned at class level all the methods, fixture will be applied to all methods in class
@pytest.mark.usefixtures("fixture name")

"""
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_script1(self):
        print("script1 executed")

    def test_script2(self):
        print("script2 executed")

    @pytest.fixture(scope='class')
    def setup(self):
        print("create driver instance")
        print("launch browser")
        yield
        print("close  browser")
