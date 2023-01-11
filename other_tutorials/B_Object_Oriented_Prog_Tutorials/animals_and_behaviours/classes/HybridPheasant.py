from random import random

from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.BlackGrouse import BlackGrouse
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.HazelGrouse import HazelGrouse


class HybridPheasant(BlackGrouse, HazelGrouse):

    combination_characteristics = []   # static variable

    def __init__(self, age, name):
        print("Inside constructor of HybridPheasant class")

    def calculate_random_age(self) -> None:
        print('Overriden method called from the concrete class HybridPheasant')
        """
        Method Resolution Order Algorithm implementation: 
        When we search for an attribute in a class that is involved in python multiple inheritance, 
        an order is followed. First, it is searched in the current class. If not found, the search 
        moves to parent classes. This is left-to-right, depth-first
        """
        super().calculate_random_age()
        # super(HazelGrouse, self).calculate_random_age()   # Proving this inheritance starts from HazelGrouse level

    """
    In Python, static methods are used when we don't want subclasses of a 
    class to change or override a specific implementation of a method
    """
    @staticmethod
    def has_disorder() -> bool:
        disorder_list = []
        if random() >= 0.6:
            print("Has one or more disorders -> True")
            disorder_list = ['heart disease']
            print("disorder_list -> " + str(disorder_list))
            return True
        else:
            print("Has one or more disorders -> False")
            print("disorder_list -> " + str(disorder_list))
            return False


"""
Python not only supports inheritance but multiple inheritance as well
Generally speaking, inheritance is the mechanism of deriving new classes
from existing ones. By doing this, we get a hierarchy of classes. In most
class-based object-oriented languages, an object created through inheritance
acquires all, although there are exceptions in some programming languages,
of the properties and behaviours of the parent object. Inheritance supports
code reusability in the subclass

Multiple inheritance is a feature in which a class can inherit attributes
and methods from more than one parent class. This concept comes with a high
level of complexity and ambiguity in situations such as the diamond problem

Java and C# do not support multi-level inheritance at a class level
(only via interfaces), while Python has a sophisticated and well-designed
approach to it

To avoid making the same call multiple times when overriding we have to use
the super function which is often used when instances are initialised with
the __init__ method
Python3 uses the so-called Method Resolution Order (MRO) which is based on
the "C3 superclass linearisation" algorithm to solve the diamond problem
"""