"""
IMPORTANT Concept
 - Functions allow us to create blocks of code that can be easily executed many times,
   without needing to constantly rewrite the entire block of code

 - Methods are functions that are built into classes

 - Creating a function requires a very specific syntax, including the def keyword,
   correct indentation, and proper structure
"""


def name_of_function(arg1):
    """
    Conventions:
     -> Snake casing is all lowercase with underscores
     -> Parenthesis at the end which are used to pass params into the function
     -> Semi-colon represents upcoming indented block
     -> Docstring is used to describe the function
     -> Code
    """
    print(f"name_of_function(arg1) was called -> {arg1}")


name_of_function("some value")
