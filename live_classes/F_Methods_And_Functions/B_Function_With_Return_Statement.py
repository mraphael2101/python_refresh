"""
 - The return keyword allows us to assign the output of a function to a new variable

 - Utilising default values

 - Another example of dynamic typing can be seen here. It is not necessary to specify
   the type of the variables arguments in the function's signature
"""


def add_function(num1=0, num2=0):
    print("Values " + str(num1) + " and " + str(num2) + " were passed in")
    result = num1 + num2
    print("The result is " + str(result))
    return result


output = add_function(1, 2)
print("Do something in the script utilising the output which is " + str(output))

output = add_function()
print("This works as default values were provided " + str(output))


def even_check(number) -> bool:
    return number % 2 == 0


print(even_check(10))
print(even_check(11))
