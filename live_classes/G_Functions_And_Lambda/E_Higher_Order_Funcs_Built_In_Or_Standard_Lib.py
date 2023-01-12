"""
- Lamda function characteristics (Syntactic Sugar):
  -> It can only contain expressions and can’t include statements in its body
    >> (lambda x: assert x == 2)(2)
        File "<input>", line 1
        (lambda x: assert x == 2)(2)
                    ^
        SyntaxError: invalid syntax

  -> It is written as a single line of execution
     Although, you can spread the expression over several lines using parentheses or
     a multiline string, it still remains a single expression

  -> It does not support type annotations

  -> It can be immediately invoked

- Benefit of using standard functions over lamda is a more precise traceback when the code fails

Python exposes higher-order functions as built-in functions or in the standard library. Examples
include map(), filter(), functools.reduce(), as well as key functions like sort(), sorted(),
min(), and max()
"""

result = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
print(result)

res = list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
print(res)

# Converts a list into a string
from functools import reduce

resu = reduce(lambda x, y: f'{x} | {y}', ['cat', 'dog', 'cow'])
print(resu)
