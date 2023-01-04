"""
 - Sets are unordered collections of unique elements

 - Meaning that there can only be one representative of the same object

"""


# Example 1
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2)  # Note that this is a duplicate value

# Example 2
my_list = [5, 5, 1, 9, 7, 5, 3, 3, 1]

if __name__ == '__main__':
    print(my_set)           # Prints {1, 2}
    print(set(my_list))     # How to convert a List into a Set
