"""
IMPORTANT -> Tuples are very similar to lists with the exception that they are immutable
            i.e., Once an element is inside a tuple it cannot be reassigned

- Tuples use parenthesis as a pose to square brackets

- They become very handy when you want to enforce control that a data structure cannot change

- To summarise, they are very similar to lists accept for the syntax (round brackets),
  and they fewer methods and are immutable
"""

my_second_tuple = (4, 5, 'Six', 4)

if __name__ == '__main__':
    print(type(my_second_tuple))
    print(my_second_tuple[1])  # Retrieve index value starting from the beginning
    print(my_second_tuple[-1])  # Retrieve index value starting from the end
    print(my_second_tuple.count(4))  # Returns how many times occurs in a tuple
    print(my_second_tuple.index(4))  # Returns the index position for the very first occurrence of the provided value
    # my_second_tuple[0] = 5    # Will raise a TypeError: 'tuple' object does not support item assignment
