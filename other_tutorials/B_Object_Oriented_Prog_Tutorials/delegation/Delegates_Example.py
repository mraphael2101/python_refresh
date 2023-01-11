"""
Delegation refers to evaluating a member (either a property or method) of one object
(the receiver) in the context of another original object (the sender). Delegation can
be done explicitly, by passing the sending object to the receiving object, which can
be done in any object-oriented language

In the below example we have passed an object's method to a function and called it twice
"""


def call_twice(f):
    f()
    f()


class Foo:
    def __init__(self, data):
        self.data = data

    def print_value(self):
        print(f"Value is {self.data}")


foo = Foo(42)   # Initialised Foo with 42

"""
A delegate allows you to pass a method around just like you would using conventional data which is 
a powerful concept

foo.print_value() returns an object of type method which can can either be called immediately,
or passed to another function to be called later 
 */                                         
"""
call_twice(foo.print_value)  
