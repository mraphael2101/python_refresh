from other_tutorials.B_Object_Oriented_Prog_Tutorials import Car


# Below, class Ford is inheriting from class Car, and we can say that a Ford 'is a' Car
class Ford(Car):

    def __init__(self, paint_colour="Black"):  # constructor overloading
        Car.__init__(self, paint_colour)

    # This derived class method overrides the base class method
    def print_colour(self, hex_arg='default'):
        print("Overriden method has Colour {} -> Hex Val {}".format(self.paint_colour, hex_arg))
