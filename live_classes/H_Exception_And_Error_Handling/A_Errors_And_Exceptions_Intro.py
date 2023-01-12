"""
In Python, there is a subtle difference between an error and an exception

Errors cannot be handled, while Python exceptions can be handled at runtime


An Error might indicate critical problems that a reasonable application should not try to catch,
while an Exception might indicate conditions that an application should try to catch.

Errors are a form of an unchecked exception and are irrecoverable like an OutOfMemoryError ,
which a programmer should not try to handle

Performing the above increases the robustness of your code

An exception is an object

We can define our own exceptions if we want to

All exceptions inherit from a built-in class called BaseException

Read exceptions from the stacktrace bottom-up
"""

def error_1():
    x = 5 / 0   # Raises ZeroDivisionByZero


def error_2():
    lst = [1, 2, 3]
    lst[3]  # Raises list index out of range


def error_3():
    d = {'a': 'my val'}
    d['b']  # Raises KeyError 'b'


def error_4():
    # print(undef_variable)   # Raises NameError 'undef_variable' is not defined


def main():
    error_1()
    # error_2()
    # error_3()
    # error_4()


if __name__ == "__main__":
    main()