class House:
    def __init__(self, no_of_rooms):
        self.no_of_rooms = no_of_rooms

    # This is an example of how to Override equals
    def __eq__(self, other):
        if not isinstance(other, House):
            return NotImplemented

        return self.no_of_rooms == other.no_of_rooms


if __name__ == '__main__':
    instance1 = House(5)
    instance2 = House(4)

    if instance1 == instance2:
        print("Both instances are equal")
    else:
        print('Both instances are not equal')
