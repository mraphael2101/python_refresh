"""
Sometimes we want to raise our own exceptions. In this example, raising an exception
when invalid arguments are declared ensures that our program only receives valid data
input
"""


class OnlyAddIntegersToList(list):

    # An example of Overriding the append method from the inherited list class
    # with my custom implementation which only accepts integers
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        super().append(integer)


def main():
    my_list = OnlyAddIntegersToList()
    my_list.append(1)   # This works
    print(my_list)
    my_list.append("")  # Generates TypeError: Only integers can be added


if __name__ == "__main__":
    main()
