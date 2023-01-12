"""
A basic example which demonstrates raising/throwing a General Exception and then
catching it. The code flow continues after the exception is caught, after the
except clause
"""


def no_return():
    print("We are about to raise an Exception")
    raise Exception("Now!")
    print("This line of code will never execute")


try:
    no_return()
except:
    print("The Exception was caught here")
print("Code flow continues from here onwards...")
