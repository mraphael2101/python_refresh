"""
In Python, most exceptions are subclasses of the exception class but this is not true
of all exceptions

Exceptions must extend BaseExceptions or one of its subclasses

SystemExit -> is raised whenever a program exits naturally typically as we called sys.exit func
It is designed to allow us to clean up code before the program terminates, or to prompt
the user to save their changes before termination.
SystemExit can also be used as an alternative to utilising the finally statement

KeyboardInterrupt -> a standard type of exception which is thrown to manage faults
with the keyboard

When we use the except: clause without specifying any type of exception then it will
catch all subclasses of BaseException

If you want to catch everything then use BaseException

Please refer to the diagrams sub-package for further details
"""