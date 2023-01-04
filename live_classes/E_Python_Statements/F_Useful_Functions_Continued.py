from random import shuffle, randint  # from random library import functions

# Built-in function to shuffle values in a list
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(my_list)
# print(my_list)

# Built-in function to generate a random number between 0 and 100
# print(randint(0, 100))

# Built-in function to capture arguments from the CLI
# Returns a String. You can cast the result by wrapping it in e.g. float(result) etc
# result = input('What is your name? ')
# print("Hello " + result)


"""
A Python list comprehension consists of brackets containing the expression, which is 
executed for each element along with the for loop to iterate over each element in 
the Python list. Python List comprehension provides a much more short syntax for 
creating a new list based on the values of an existing list.
"""
#
celcius = [0, 10, 20, 34.5]
fahrenheight = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheight)

# The below code can be optimised/expressed using a list comprehension
fahrenheight = []
for temp in celcius:
    fahrenheight.append(((9 / 5) * temp + 32))
print(fahrenheight)
