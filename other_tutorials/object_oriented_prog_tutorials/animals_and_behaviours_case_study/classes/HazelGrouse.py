from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.Bird import Bird
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.interfaces.IHop import FormalInterfaceIHop


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
