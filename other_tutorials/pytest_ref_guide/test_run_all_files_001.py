"""
    1) Any pytest file should start with test_ or end with _test
    2) pytest method names should start with test
    3) py.test command executes all pytest methods in current directory [py.test -v -s]
    4) -s logs in out put
    5) -v stands for more info metadata
    6)to run specific file  py.test <filename> -v -s

"""


def test_script1():
    print("script1 executed")
    assert 5 + 1 == 6


def test_script2():
    print("script2 executed")
    assert 5 + 1 == 7
