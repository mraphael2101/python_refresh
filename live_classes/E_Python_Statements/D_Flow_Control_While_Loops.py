"""
Pseudocode:
while some_boolean_condition:
    #do something
else:
    #do something different

There are three keywords which can be associated with loops which are:
    break    -> Breaks out of the current closest enclosing loop
    continue -> Goes to the top of the closest enclosing loop
    pass     -> Does nothing
"""

x = 1
while x < 5:  # Condition must evaluate to true to enter into the loop
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print(f'x is not less than {x}. Hence, this statement was printed')


"""
 - Effect of continue keyword is to skip the current iteration
 - Effect of break keyword is to exit the loop
"""
my_str = "test automation class"
for letter in my_str:
    if letter == 'a':
        continue
    if letter == 'l':
        break
    print(letter)
