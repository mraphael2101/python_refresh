"""
- Everything in Python is an object just like in JS
- It is possible to execute the below function without it being bound to an object
"""

def print_base_class_method():
    print("This method is unique to the base class")


class Car:
    # Python oop supports B_Objects_And_Data_Structures at either a class level or an instance level
    # Class level is basically a default value that will not need to be changed for every instance
    driving_mode = "Manual Transmission"

    # The self keyword creates an instance of the class and allows it to refer to itself
    # Init method is called by default when you create an instance of the class
    def __init__(self, colour):
        self.colour = colour

    # We can override a default argument value like this
    def print_colour(self, hex_arg='default'):
        print("Colour passed into the constructor was {} -> Hex Val {}".format(self.colour, hex_arg))
