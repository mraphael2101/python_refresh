"""
You need to know how to execute code regardless of whether or not an exception has occurred

Should be able to specify code that should be executed only if an exception does not occur

Two more keywords finally and else can provide the missing pieces

The below example demonstrates randomly picking an exception to throw and raises it

If no exception is raised then both the else and finally statements are executed

Examples of when you might use the finally block:
  - Cleaning up an open database connection
  - Closing an open file
"""

import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice('An error')
except ValueError:
    print('Caught a ValueError')
except TypeError:
    print('Caught a TypeError')
except Exception as e:
    print("Caught some other error: %s" % e.__class__.__name__)

# Note: The else statement will not be executed if an exception is raised and handled
else:
    print("This code called if there is no exception")

finally:
    print("This cleanup code is always called")
