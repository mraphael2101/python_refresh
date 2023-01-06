from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.BlackSparrow import BlackSparrow
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.Eagle import Eagle


class CrossBreed(BlackSparrow, Eagle):

    def __init__(self, age, name):
        print("Inside constructor of CrossBread class")

    def calculate_random_age(self) -> None:
        print('Overriden method called from the concrete class CrossBread')
        # Method Resolution Order Algorithm implementation
        super().calculate_random_age()

    """
    In Python, static methods are used when we don't want subclasses of a 
    class to change or override a specific implementation of a method
    """
    @staticmethod
    def has_disorder() -> bool:
        return True


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