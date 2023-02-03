"""
__call__ in Python
Python has a set of built-in methods and __call__ is one of them. The __call__ method
enables Python programmers to write classes where the instances behave like functions
and can be called like a function. When the instance is called as a function; if this
method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
"""


class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")


# Instance created
e = Example()

# __call__ method will be called
e()
