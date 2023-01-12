"""

"""


class OnlyAddIntegersToList(list):

    # Overriding the append method from the list class with my custom implementation
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
