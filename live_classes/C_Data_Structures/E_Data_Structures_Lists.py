"""
- A list is an ordered sequence of elements which supports indexing and slicing in the same
  way as for String

  IMPORTANT:
  A list is a type of object / data structure in Python that is a mutable, or changeable,
  ordered sequence of elements. Each element or value that is inside a list is called an item
"""

my_int_list = [1, 2, 3]
my_string_list = ['night night', 'good morning', 'hello']
my_varied_list = ['A string', 100, 3.14]

# It is very easy to perform concatenation of lists in Python.
# This can be achieved by using the plus operator
my_new_list = my_int_list + [4, 5, 6]

if __name__ == '__main__':
    # print(len(my_varied_list))  # Note that the counter starts from 1 and not from 0
    # print(my_int_list[0:1])  # Returns [1]
    # print(my_new_list)  # Returns [1, 2, 3, 4, 5, 6]
    # my_int_list[0] = 9  # Reassigning new values to a list element is as easy as
    # print(my_int_list)
    # my_int_list.append(4)  # Lists are dynamic and can change in size. You can add an extra element like this
    # print(my_int_list)
    # popped_item = my_int_list.pop()  # The pop method can be used to pop-off items from the end of a list
    # print(my_int_list)
    # print("Popped item = " + str(popped_item))
    #
    # my_int_list.pop(1)  # To remove an element at a specific index starting from index 0
    # print(my_int_list)  # [9, 2, 3] mutates to -> [9, 3]
    # # Reverse indexing also works for a list just like it does for String
    #
    # # The sort() method reorders a string list in alphabetical order
    # my_string_list.sort()
    # print(my_string_list)  # As you can see the list name is sorted
    my_int_list.reverse()
    print(my_int_list)
