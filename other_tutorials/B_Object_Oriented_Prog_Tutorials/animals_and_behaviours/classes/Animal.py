from abc import ABC, abstractmethod

"""
- Use the abc module support framework as an enabler to implement Abstract Base Classes
- Abstraction is an OO term related to encapsulation and information hiding
- Abstraction means dealing with the level of detail that is most appropriate for 
  a given task
- It is the process of extracting a public interface from the inner details
- It is the process of encapsulating information with separate public and 
  private interfaces. The private interfaces can be subject to information hiding
- Our models should be understandable to other objects that interact with them  
- Abstract base classes define a set of methods and properties that a class must implement
  in order to be considered a duck-type instance of that class, but it must supply all the 
  appropriate methods (no inheritance required which is the benefit)

- In the case of Animals, it doesn't really make sense to provide a default implementation
  of the below methods
"""


class Animal(ABC):

    def __init__(self, age, name=None):  # Constructor overloading
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
