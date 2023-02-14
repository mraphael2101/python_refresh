"""
if usefixture is mentioned at class level all the methods, fixture will be applied to all methods in class
@pytest.mark.usefixtures("fixture name")

"""
import pytest


class TestExample:

    def test_script1(self):
        print("script1 executed")

    def test_script2(self, multiple_sets_data):
        print("**********")
        print(multiple_sets_data)
