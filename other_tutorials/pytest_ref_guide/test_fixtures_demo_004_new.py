"""
fixtures in pytest are a way to set up preconditions for your tests.
They can be used for various tasks such as creating test data, initializing resources, and cleaning up after tests.
You can define fixtures using the @pytest.fixture decorator, and then use them in your tests by passing them as function arguments.
--> to group set of tests @pytest.mark.smoke and then run with -m


"""
import pytest


def test_script1(setup):
    print("script1 executed")


def test_script2(setup):
    print("script2 executed")


