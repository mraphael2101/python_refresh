"""
Below are examples of exceptions. They can be handled at runtime and are not unconditionally
fatal

Refer to the Python Docs for more info:
https://docs.python.org/3/library/exceptions.html?highlight=exceptions#exception-hierarchy
"""


def error_1():
    x = 5 / 0   # Raises ZeroDivisionByZero


def error_2():
    lst = [1, 2, 3]
    lst[3]  # Raises list index out of range


def error_3():
    d = {'a': 'my val'}
    d['b']  # Raises KeyError 'b'


# def error_4():
#     print(undef_variable)   # Raises NameError 'undef_variable' is not defined


def main():
    # error_1()
    # error_2()
    error_3()
    # error_4()


if __name__ == "__main__":
    main()