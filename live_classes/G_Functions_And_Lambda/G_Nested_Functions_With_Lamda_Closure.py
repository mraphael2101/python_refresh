"""
On line 6, outer_func() returns a lambda and assigns it to the variable closure.
On line 3, the body of the lambda function references x and y. The variable y
is available at definition time, whereas x is defined at runtime when outer
_func() is invoked.

In this situation, both the normal function and the lambda behave similarly.
In the next section, you’ll see a situation where the behavior of a lambda
can be deceptive due to its evaluation time (definition time vs runtime).
"""


def outer_func(x):
    y = 4
    return lambda z: x + y + z


for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")