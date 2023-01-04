"""
If you use single quotes within a String literal then you should ideally have String quotes on the outside
otherwise you need to use Character Escape Sequences

Character Escape sequences translate into commands e.g. \n will result in a new line being printed
"""

janet = "I'm going for a run \ntomorrow in Hyde Park"
alex = "I'm going for a run \ttomorrow in Central Park"

if __name__ == '__main__':
    print(janet)
    print(alex)
    print(len(alex))  # Prints the no of chars in a String
    print(alex[0])  # Returns the char representative of the index number provided
    print(alex[-1])  # Slice notation -> Returns the char representative of the string length minus 1
    print(alex[21:])  # Returns the char sequence from the start index until the end
    print(alex[:20])  # Returns the char sequence from the end of the string traversing backwards
    print(alex[15:20])  # Returns the substring between the start and end index
    print(alex[::2])  # Parses the string and returns a list of chars with a jump sequence of 2
    print(alex[::-1])  # Parses the string and returns the reverse sequence of chars

    """
    Strings are immutable meaning that they cannot change by reassignment
    """
    car_model = "CL"
    # car_model[0] = 'H'   # Uncommenting this line will throw a Type error for the above reason

    # Examples of String concatenation in different ways
    modified_car_model = car_model
    modified_car_model += "X"
    modified_car_model2 = car_model + "S"
    print(modified_car_model)
    print(modified_car_model2)

    # Examples of some String methods
    # Press the dot operator on a String variable
    print(modified_car_model.lower())  # Must have the parenthesis at the end
    greeting = "Hello World"
    result = greeting.split("o")  # Returns a list based on blank separator or whatever is provided
    print(result)
    print(result[0])

    # An example of how to substitute values using the String format() method
    print("Substituting a value into this -> {} String".format('INSERTED'))
    print("The {0} {2} {2}".format('Quick', 'Brown', 'Fox'))


