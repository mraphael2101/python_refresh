from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.Bird import Bird
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.interfaces.ICanFly import \
    InformalInterfaceICanFly


class BlackGrouse(Bird, InformalInterfaceICanFly):
    """
    BlackGrouse is a subclass of Bird and also implements the InformalInterfaceICanFly
    which provides an implementation of the interface’s methods
    """

    def __init__(self, age, name):
        self.__age = age
        print("Inside constructor of BlackGrouse class")

    def calculate_random_age(self) -> None:
        self.__age = 0
        print('Overriden method from concrete class Bird. Called in class BlackGrouse -> age {}'.format(self.__age))
        super().calculate_random_age()

    def ascend(self, altitude: float) -> float:
        print("Overriden method (1 of 2) from InformalInterfaceICanFly class")
        return 1.01

    """
    Encapsulation prevents unwanted access to sensitive data and hide information through access modifiers 
    while also reducing erroneous human changes
    """
    def get_age(self):
        return self.__age

    def set_age(self, val):
        self.__age = val
