"""
- Many objects in Python are 'iterable' meaning that we can iterate over them

- e.g., every element in a list or every character in a String

- Emphasis that indentation is very important as it can mean the difference between
  performing an operation every time, or just once
"""

my_string = "Hello World"
for ele in my_string:
    print(ele)

# You can use string functions to manipulate output when traversing using loops
another_string = 'Welcome to 2023. I hope you had a well rested break.'
for word in another_string.split():
    print(word)

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in int_list:
    if num % 2 == 0:  # Modulus expression
        print(f'Remainder is O. The No entered was -> {num}')
    else:
        print(f'Remainder is not 0. The No entered was -> {num}')

# Example of returning tuples inside a list
list_containing_tuples = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
print(len(list_containing_tuples))
for tupe in list_containing_tuples:
    print(tupe)

# This approach is known as Tuple unpacking
for (x, y) in list_containing_tuples:
    print(y)

# Traversing through a Dictionary (Prints value and key pairs)
# Also try with .keys() or .values()
my_dict = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for item in my_dict.items():
    print(item)

# Allows you to extract the key and/or value from the dictionary
for key, value in my_dict.items():
    print(value)
