"""
   1)to group set of tests @pytest.mark.smoke and then run with -m
  2) To skip any test method @pytest.mark.skip

"""
import pytest


@pytest.mark.regression
def test_script1():
    print("script1 executed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.dailyrun
def test_script2():
    print("script2 executed")


@pytest.mark.smoke
def test_script3():
    print("script3 executed")
    assert 1 + 1 == 2, "assertion error message"


@pytest.mark.smoke
def test_script4():
    print("script3 executed")
    assert 1 + 1 == 3, "assertion error message"
