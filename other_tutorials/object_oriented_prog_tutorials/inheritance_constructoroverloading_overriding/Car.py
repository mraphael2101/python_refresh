"""
- Everything in Python is an object just like in JS
- It is possible to execute the below function without it being bound to an object
"""


def print_base_class_method():
    print("This method is unique to the base class")


class Car:
    paint_colour = "Metalic Blue"

    # The self keyword creates an instance of the class and allows it to refer to itself
    # Init method is called by default when you create an instance of the class
    def __init__(self, paint_colour):
        Car.paint_colour = paint_colour

    # We can override a default argument value like this
    def print_colour(self, hex_arg='default'):
        print("Colour passed into the constructor was {} -> Hex Val {}".format(self.paint_colour, hex_arg))
