"""
Higher Orders Functions are functions that perform operations on other functions. In this definition,
operations can mean taking one or more functions as an argument OR returning a function as the result.
It doesn't have to do both. Doing one or the other qualifies a function as a higher order function.

A lambda function can be a higher-order function by taking a function (normal or lambda) as an
argument like in the following contrived example
"""

high_ord_func = lambda x, func: x + func(x)  # higher order function declaration

# Pay attention to the syntax -> Substitute the value of x into x + func(x)
result = high_ord_func(2, lambda x: x * x)
print(result)  # Prints 6

result = high_ord_func(2, lambda x: x + 3)
print(result)  # Prints 7
