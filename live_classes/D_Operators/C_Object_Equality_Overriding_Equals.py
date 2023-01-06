"""
Know the difference between equality and identity
 -> == compares 2 objects for equality
 -> is compares 2 objects for identity

For immutable types, operations that compute new values may actually return a reference to any
existing object with the same type and value, while for mutable objects this is not allowed.

Objects of built-in types like (int, float, bool, str, tuple, unicode) are immutable. Objects
of built-in types like (list, set, dict) are mutable. Custom classes are generally mutable
"""


class House:
    def __init__(self, no_of_rooms):
        self.no_of_rooms = no_of_rooms

    """
    Overriding equals is necessary as the default implementation of Python will consider
    that two objects are different even if they have the same values. The only exception
    to this rule is if you are utilising a str class which either has a single character
    or multiple chars which equal another string either by reassignment or by 
    declaration/initialisation which will return true.
    Below is an example of how to Override equals
    """
    def __eq__(self, other):
        print("Id of instance1 -> " + str(id(self)))
        print("Id of instance2 -> " + str(id(other)))
        print("instance1 has the same Id as instance2 -> " + str(self is other))

        if self.__class__ == other.__class__:
            return True
        if other is None:
            return False
        if self.__class__ != other.__class__:
            return False
        return self.no_of_rooms == other.no_of_rooms


if __name__ == '__main__':
    """
    If we create 2 mutable objects independently, they will definitely end up in different 
    memory addresses, thus have different ids
    """
    instance1 = House(5)
    instance2 = House(5)

    if instance1 == instance2:
        print("Both instances are equal")
    else:
        print('Both instances are not equal')