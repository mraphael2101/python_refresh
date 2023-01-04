# It is possible to run Python scripts and modules from an interactive session using Jupyter
# To install and run Jupyter from the terminal type:
# 1) pip install jupyterlab
# 2) jupyter-lab

# An example of how to import a script using the Jupyter interpreter:
# >>> from live_classes.B_Methods_Of_Code_Execution import *
# >>> import sys
# >>> for path in sys.path:
#       print(path)
# Output:
# /Users/rapham/Documents/py_workspace/python_oop
# /usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python310.zip
# /usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10
# /usr/local/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-download

# An example of how to use the built-in function exec() to dynamically execute Python code from the interpreter
# >>> exec(open('A_Execute_Program_Via_Main.py').read())
# Output:
# The main method was executed
# The value of __name__ is: '__main__'


# An example of how to import a module using the Jupyter interpreter:
# >>> import importlib
# >>> importlib.import_module('other_tutorials')
# Output:
# <module 'other_tutorials' from '/Users/rapham/Documents/py_workspace/python_oop/other_tutorials/__init__.py'>


# Reimporting modules
# Once you’ve imported a module for the first time, you won’t be able to continue using import to run it.
# In this case, you can use importlib.reload(), which will force the interpreter to re-import the module again
# Example
# import other_tutorials
# importlib.import_module('other_tutorials')
# Output:
# <module 'other_tutorials' from '/Users/rapham/Documents/py_workspace/python_oop/other_tutorials/__init__.py'>


# How to Run modules without importing them. You can do either of the following:
# >>> import runpy
# >>> runpy.run_module(mod_name='other_tutorials')
# >>> runpy.run_path(path_name='give/path/A_Execute_Program_Via_Main.py')
