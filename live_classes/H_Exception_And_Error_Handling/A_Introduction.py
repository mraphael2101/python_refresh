"""

Today we will focus on the details of how to raise and handle exceptions which
will assist to make our code more robust and to prevent potential failures that would
otherwise cause a program to stop in an uncontrolled manner

Exceptions are a powerful way to communicate unusual circumstances or error conditions
without requiring a calling function to explicitly check return values



In Python, there is a subtle difference between an error and an exception

An Error might indicate critical problems that a reasonable application should not try to catch,
while an Exception might indicate conditions that an application should try to catch at runtime

Errors are a form of an unchecked exception and are irrecoverable like an OutOfMemoryError
Even if the syntax of a statement or expression is correct, it may still cause an error when executed.

Python exceptions are types of errors that are detected during runtime and are not unconditionally fatal



An exception is an object

We can define our own exceptions if we want to

All exceptions inherit from a built-in class called BaseException

When an exception occurs you generally read the stacktrace from the bottom-up

"""