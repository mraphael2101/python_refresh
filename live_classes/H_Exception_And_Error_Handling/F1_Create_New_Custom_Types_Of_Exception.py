"""
If you want to define your own custom exception (if none of the built-in exceptions
are suitable) all you have to do is to inherit from the Exception class

The name of the class is usually designed to communicate what went wrong
"""


class InvalidWithdrawal(Exception):
    pass


# You can raise the newly defined exception like this
raise InvalidWithdrawal("You don't have 50 GBP in your account")



