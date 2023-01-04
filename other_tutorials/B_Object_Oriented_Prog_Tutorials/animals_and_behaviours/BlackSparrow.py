from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.ICanFly import InformalInterfaceICanFly


class BlackSparrow(Bird, InformalInterfaceICanFly):
    """
    BlackSparrow is a concrete class (a subclass of Bird && InformalInterfaceICanFly
    which provides an implementation of the interface’s methods)
    """

    def __init__(self, age, name):
        print("Inside constructor of BlackSparrow class")

    def calculate_random_age(self) -> None:
        self.age = 0
        print('Overriden method from concrete class Bird. Called in class BlackSparrow -> age {}'.format(self.age))
        super(BlackSparrow, self).calculate_random_age()

    def ascend(self, altitude: float) -> float:
        print("Overriden method (1 of 2) from InformalInterfaceICanFly class")
        return 1.01
