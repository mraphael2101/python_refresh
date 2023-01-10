"""
Python interfaces are used to help determine what class you should use to
tackle the current problem and to avoid confusion from having similar classes
which are unrelated

In OOP, an Interface is a description of all functions that an object must have
in order to be an "X"

Interfaces in Python are handled differently than in most other languages.
Python does not have an interface keyword

Python has an Informal interfaces concept which is when a class defines methods
that can be optionally implemented. This feature is often used for smaller projects
that have a small code base and a limited no of programmers
"""


class InformalInterfaceICanFly:
    def ascend(self, altitude: float) -> float:
        pass

    def descend(self, altitude: float) -> object:
        pass


"""
Interfaces are not necessary in Python. This is because Python has proper multiple inheritance 
and also duck typing, which means that the places where you must have interfaces in Java, 
are not necessary in Python.

That said, there are still several uses for interfaces. Some of them are covered by Python's 
Abstract Base Classes, which are useful if you want to make base classes that cannot be 
instantiated, but provide a specific interface or part of an implementation.

"""
