from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.IHop import FormalInterfaceIHop


class CPomarinaEagle(Bird, FormalInterfaceIHop):
    def __init__(self, age, name):
        print("Inside constructor of Eagle class")

    def calculate_random_age(self) -> None:
        self.age = 0
        print('Overriden method from concrete class Bird. Called in class Eagle -> age {}'.format(self.age))
        # Method Resolution Order Algorithm implementation
        super(CPomarinaEagle, self).calculate_random_age()

    def get_average_hop_height(self) -> float:
        print("Overriden method get_average_hop_height() from FormalInterfaceIHop")
        return 0.33

    def get_max_hop_height(self) -> float:
        print("Overriden method get_max_hop_height() from FormalInterfaceIHop")
        return 0.99
