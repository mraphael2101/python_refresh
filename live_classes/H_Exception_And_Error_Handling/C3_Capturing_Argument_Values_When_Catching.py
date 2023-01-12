"""
The below example demonstrates the syntax of capturing an exception
as a variable uses the as keyword
"""


def division_calc(arg1):
    try:
        return 100 / arg1

    # Doing this allows us to access the argument(s) that were passed
    # in if an exception was thrown
    except Exception as e:
        print(e.args)


division_calc("s")