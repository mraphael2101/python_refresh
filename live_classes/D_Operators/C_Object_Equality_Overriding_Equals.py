class House:
    def __init__(self, no_of_rooms):
        self.no_of_rooms = no_of_rooms

    """
    Overriding equals is necessary as the default implementation of Python will consider
    that two objects are different even if they have the same values. The only exception
    to this rule is if you are utilising a String class which either has a single character
    or multiple chars which equals another string either by reassignment or by 
    declaration/initialisation which will return true.
    This is an example of how to Override equals
    """
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return True
        if other is None:
            return False
        if self.__class__ != other.__class__:
            return False
        return self.no_of_rooms == other.no_of_rooms


if __name__ == '__main__':
    instance1 = House(5)
    instance2 = House(5)

    if instance1 == instance2:
        print("Both instances are equal")
    else:
        print('Both instances are not equal')
