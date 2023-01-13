"""
It is possible to define a varying number of arguments into the constructor to
include additional information

Exceptions should be easy to handle and easy to see how to fix the error
"""


class InvalidWithdrawal(Exception):

    # The __init__ method is designed to accept any arguments and to store them
    # as a tuple in an attribute named args
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}")
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


"""
Defining your own custom exceptions is especially useful when creating a framework,
library, or API that is intended for access by other programmers 
"""

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrawal is "
          "more than your balance by "
          f"${e.overage()}")
