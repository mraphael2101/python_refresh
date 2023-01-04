"""
-> Python has 4 primitives which are:
     a) Integers,
     b) Float,
     c) Strings
     d) Boolean


-> We can declare variables and/or initialise them by assigning a value
    - It is possible to declare a variable without assigning it a value or a type
    - It is possible to declare a variable and to initialise it on the same line


->  Rules when declaring variable names:
     - Names cannot start with a Number
     - There can be no spaces in the name (use underscore instead)
     - The following character symbols are not allowed :"',<>/?()!@#$%^&~-+
     - Global variable names are declared in all caps
     - General naming convention for is lowercase delimited by underscore
     - Avoid using reserved keywords like 'list' and 'str'


-> Python supports:
    - Dynamic Typing means that you can reassign values to different data types on the fly
    - A Dynamically typed language determines the variable type at runtime rather than before
    - Removes protection from Runtime Errors provided by statically typed languages
    - Introduces flexibility by not having to specify argument types in functions and methods
"""

# An Example of Dynamic Typing and how to reassign a variable
my_dogs = ['Cubie', 'Minty']
print(my_dogs)
my_dogs = 2
print(my_dogs)
my_dogs + my_dogs
my_dogs
my_dogs = my_dogs + my_dogs
my_dogs
type(my_dogs)

dynamic_typed_tuple = (4, 5, 'Six', 4)  # Dynamically Typed (not necessary to delare the type of variable upfront)

static_typed_tuple: tuple[int, int, int] = (1, 2, 3)  # Example of Statically Typed
