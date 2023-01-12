"""
In the Python console demonstrate:
    1 < 2 > 3            --> Chaining approach
    1 < 2 and 2 > 3      --> Logical operators approach preferred as more readable
    'h' == 'h' and 2 == 2
    1 == 1 or 2 == 1
"""


class LogicalOperators:
    a = 5
    b = 6

    # Example of using the not operator
    if not a == b:
        print("Result inverted and therefore this statement was executed")

    if not 400 > 401:
        print("Result inverted: Expression evaluated to True")


if __name__ == '__main__':
    instance = LogicalOperators