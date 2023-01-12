"""
We should catch specific types of Exceptions - we might have a code that raises both
TypeError and ZeroDivisionError. We might want to catch ZeroDivisionError but let
TypeError propagate

Only the first matching exception clause is run, even if more than one of them fits
"""


def division_calc(arg1):
    try:
        if arg1 == 42:
            raise ValueError("42 is an unlucky number for some")

        return 100 / arg1

    except ZeroDivisionError:
        return "ZeroDivisionError -> Mathematicians are always trying to find answers to interesting math problems"
    except TypeError:
        return "TypeError -> Enter a numerical value"
    except ValueError as e:
        print("ValueError -> No, No, not 42")
        raise  # This keyword will raise this exception again


# The code will continue to execute after an exception occurs and is handled
for val in (0, "d", 50.1, 42):
    print("Testing the value -> {}".format(val))
    print(division_calc(val))
