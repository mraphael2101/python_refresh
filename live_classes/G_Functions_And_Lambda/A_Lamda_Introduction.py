"""
Python is not inherently a functional language, but it adopted some functional concepts
like map(), filter(), reduce(), and the lambda operator were added to the language

Python lambdas are little, anonymous functions, subject to a more restrictive
but more concise syntax than regular Python functions

Lambda Calculus (also referred to as lambda functions / abstractions)
- Python has its roots in lambda calculus which is based on pure abstraction and is
  a model of computation
- The lambda calculus philosophy is a declarative approach of programming that
  emphasizes abstraction, data transformation, composition, and purity (no state and
  no side effects)
- In contrast to, Imperative languages that involve programming with statements, driving
  the flow of the program step by step with detailed instructions (an approach promotes mutation
  and requires managing state)
"""

"""
Python is not inherently a functional language, but it adopted some functional concepts
like map(), filter(), reduce(), and the lambda operator were added to the language

Python lambdas are little, anonymous functions, subject to a more restrictive
but more concise syntax than regular Python functions
"""

# The identity function, a function that returns its argument
def identity(x):
    return x

"""
- The above is equivalent to the below lambda expression
- A bound variable is an argument to a lambda function (the value before the colon)
- A free variable is not bound and may be referenced in the body of the expression
  (the value after the colon)
"""
lambda x: x