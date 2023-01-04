from typing import Final

"""
Unlike other languages it is not possible to enforce the behaviour of the final or readonly concept in Python.
This is because a variable that is declared as final can be overriden or reassigned a new value 
However, we can indicate to programmers that a variable is a constant by utilising upper case naming convention.

Furthermore, we can log the error by using utilities such as mypy which is a static type checker
To install:
python3 -m pip install mypy
To execute:
mypy _04b_DataStructures_Constants.py
"""

if __name__ == '__main__':
    PI: Final[int] = 3.14
    PI = 3.15
    print(PI)
