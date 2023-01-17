"""

Raising and handling exceptions assists us to make our code more robust and to prevent
potential failures that would otherwise cause a program to stop in an uncontrolled manner

Exceptions are a powerful way to communicate unusual circumstances or error conditions
without requiring a calling function to explicitly check return values

Errors are unrecoverable, Exceptions are routine:
---------------
"""

"""
  -> Languages like Java build the distinction into the language
  -> Python treat them as synonyms (there is a
     subtle difference between an error and an exception)

An Error might indicate critical problems that a reasonable application should NOT try to catch,
while an Exception might indicate conditions that an application should try to catch at runtime

Errors are a form of an unchecked exception and are irrecoverable. An example of one is MemoryError

Python exceptions are types of errors that are detected during runtime and are not completely fatal
Even if the syntax of a statement or expression is correct, it may still cause an error when executed
-----------------


- An exception is an object
- In Python, all exceptions inherit from a built-in class called BaseException
- We can define our own exceptions if we want to
- When an exception occurs you generally read the stacktrace from the bottom-up

"""