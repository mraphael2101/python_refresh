"""
The following terms may be used interchangeably: Anonymous functions, Lambda functions,
Lambda expressions, Lambda abstractions, Lambda form, Function literals

In Python, an anonymous function is created with the lambda keyword
"""

add_one = lambda x: x + 1
print(add_one(1))

add_two_vars = lambda x, y: x + y
print(add_two_vars(1, 4))

"""
You can apply a function to an argument by surrounding it and its argument with parentheses
The below lamda expression has been bound to a variable
"""

func_applied = (lambda x: x + 1)
print(func_applied(2))

"""
-> Syntax of a lamda with multiple arguments. Note, no parenthesis surrounds the arguments
-> The lambda function assigned to full_name takes two arguments and returns a string
-> Calling the function is done exactly like a normal Python function, with parentheses 
   surrounding the arguments
"""

full_name = lambda first, last: f'Full name: {first} {last}'
print(full_name('guido', 'van rossum'))

# A lamda expression using modulus to determine if a number is odd or even
print((lambda x: (x % 2 and 'odd' or 'even'))(2))
