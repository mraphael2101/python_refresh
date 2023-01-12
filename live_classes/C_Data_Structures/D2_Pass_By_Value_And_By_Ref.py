"""
- When you give function parameters via reference, you're just passing references to
  values that already exist. When you pass arguments by value, on the other hand, the
  arguments become independent copies of the original values

- Pass by value means to provide an argument to a function

- Pass by reference means that the argument that has been passed to the function is
  a reference to a variable that is already existing in memory
"""


"""
Pass by value:
 - In the example below, the variable a which points to the string is mutable
 - The string objects themselves are immutable
"""
a = "Foo"   # a now points to 'Foo'
b = a       # b points to the same 'Foo' that a points to
a = a + a   # a points to the new string 'FooFoo', but b still points to the old 'Foo' print a
print(b)    # Observe that b hasn't changed, even though a has
print(a)


"""
Pass by reference:
 - In the example below, the method passes a reference to the original arguments, 
   and any operation performed on the parameter affects the actual value. It alters 
   the value in both function and globally
"""


def function(val):
    val.append('B')
    print("Inside function call", val)


val = ['A']
print("Before function call", val)
function(val)
print("After function call", val)