# A piece of code can reside in any of the following:
# File: Typically, a Python file is any file that contains code. Most Python files have the extension .py.
# Script: A Python script is a file that you intend to execute from the command line to accomplish a task.
# Module: A Python module is a file that you intend to import from within another module or a script, or
# from the interactive interpreter


# The Python interpreter executes scripts starting at the top of the file,
# and there is no specific function that Python automatically executes like in Java or C#
# There are two primary ways that you can instruct the Python interpreter to execute or use code
# 1) You can execute the Python file as a script using the command line
# 2) You can import the code from one Python file into another file or into the interactive interpreter
def main():
    print("The main method was executed")


# No matter which way of running your code you’re using, Python defines a special variable called __name__
# that contains a string whose value depends on how the code is being used i.e. the selected context
# In Python, repr() displays the printable representation of an object
if __name__ == "__main__":
    main()
    print("The value of __name__ is:", repr(__name__))
