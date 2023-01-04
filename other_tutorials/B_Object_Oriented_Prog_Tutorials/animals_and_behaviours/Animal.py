from abc import ABC, abstractmethod

"""
1) Abstract base classes define a set of methods and properties that a class must
implement in order to be considered a Duck-type instance of that class.
2) Use abc module support framework as an enabler to implement Abstract Base Classes
This is how you define one. The example also demonstrates Constructor Overloading
"""


class Animal(ABC):
    def __init__(self, age, name=None):
        print("Inside constructor of the Animal class")
        self.age = age
        self.name = name
        if self.name is not None and self.name != "":
            print("A derived class of Animal now exists with the name {}".format(self.name))
        else:
            self.name = "Default Firstname Lastname"
            print("A derived class of Animal now exists without a name. Assigning a default name")
        super().__init__()

    # An abstract method can have implementation or can just be a signature

    @abstractmethod
    def calculate_random_age(self) -> None:
        print("Abstract method calculate_random_age() implementation")

    @abstractmethod
    def generate_security_code(self) -> int:
        return 1111

    def get_age(self):
        return self.age

    def set_age(self, val):
        self.age = val
