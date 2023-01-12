"""
In Python, a decorator is the implementation of a pattern that allows
adding a behavior to a function or a class. It is usually expressed
with the @decorator syntax prefixing a function.

In the example, some_decorator() is a function that adds
a behavior to decorated_function()
"""


def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps


@some_decorator     # This decorator adds an extra behavior
def decorated_function(x):
    print(f"With argument '{x}'")


def main():
    decorated_function('Some value')


if __name__ == "__main__":
    main()