"""
if usefixture is mentioned at class level all the methods, fixture will be applied to all methods in class
@pytest.mark.usefixtures("fixture name")

"""
import pytest
from selenium import webdriver


class TestExample:

    def test_script1(self, userdata):
        print("**********")
        print(userdata[0])
        print(userdata[1])
        print(userdata[2])

    def test_script2(self, datadriven):
        print("**********")
        print(datadriven)

    def test_script3(self, userdata, datadriven):
        print("**********")
        print(userdata)
        print(datadriven)


    @pytest.fixture()
    def userdata(self):
        return ["Murali", "Mark", "Matt"]

    @pytest.fixture(params=[1,2,3])
    def datadriven(self, request):
        return request.param


