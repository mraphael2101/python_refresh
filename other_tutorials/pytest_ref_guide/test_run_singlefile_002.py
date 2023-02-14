"""
    6)to run specific file  py.test <filename> -v -s
    7)to run specific files using regular expressions use -k
            py.test -k <partialfilename> -v -s
            py.test -k sports -v -s test_run_singlefile_002.py


"""


def test_broadband_001():
    print("script1 executed")
    assert 5 + 1 == 6


def test_sports_002():
    print("script2 executed")
    assert 5 + 1 == 6


def test_broadband_003():
    print("script3 executed")
    assert 5 + 1 == 6


def test_sports_004():
    print("script2 executed")
    assert 5 + 1 == 6
