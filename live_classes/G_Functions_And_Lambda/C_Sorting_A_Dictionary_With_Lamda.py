"""
Example of using Lambda expression to sort a dictionary based on the values
"""

my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict_by_value = {k: v for k, v in sorted(my_dict.items(), key=lambda arg: arg[1])}
sorted_dict_by_key = {k: v for k, v in sorted(my_dict.items(), key=lambda arg: arg[0])}

if __name__ == '__main__':
    # print(sorted_dict_by_value)
    print(sorted_dict_by_key)