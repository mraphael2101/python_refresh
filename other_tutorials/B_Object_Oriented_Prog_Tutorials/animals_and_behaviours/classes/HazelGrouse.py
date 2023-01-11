from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.interfaces.IHop import FormalInterfaceIHop


class HazelGrouse(Bird, FormalInterfaceIHop):
    def __init__(self, age, name):
        print("Inside constructor of HazelGrouse class")

    def calculate_random_age(self) -> None:
        self.age = 0
        print('Overriden method from concrete class Bird. Called in class HazelGrouse -> age {}'.format(self.age))
        # Method Resolution Order Algorithm implementation
        super().calculate_random_age()

    def get_average_hop_height(self) -> float:
        print("Overriden method get_average_hop_height() from FormalInterfaceIHop")
        return 0.33

    def get_max_hop_height(self) -> float:
        print("Overriden method get_max_hop_height() from FormalInterfaceIHop")
        return 0.99
