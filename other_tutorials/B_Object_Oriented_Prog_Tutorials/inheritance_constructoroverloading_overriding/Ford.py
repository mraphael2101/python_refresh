from other_tutorials.B_Object_Oriented_Prog_Tutorials import Car

"""
- In this example, class Ford is inheriting from class Car
- In Python it is not necessary to have multiple constructors like you do in Java, C#, or TS
"""


class Ford(Car):

    # In Python, the below line of code is how to go about constructor overloading
    def __init__(self, paint_colour="Black"):
        Car.__init__(self, paint_colour)

    # This derived class method overrides the base class method
    def print_colour(self, hex_arg='default'):
        print("Overriden method has Colour {} -> Hex Val {}".format(self.paint_colour, hex_arg))