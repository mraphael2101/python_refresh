"""
- Dictionaries are a construct based on key and value pairs

- Lists are ordered in sequence. Dictionaries are not. However, they can be sorted using function/lambda.
"""

my_dict = {'key1': 'a', 'key2': 'b'}

fruits_dict = {'apple': 2.99, 'oranges': 1.99, 'pears': 0.99}


class Popo:
    my_attr = "some value"


class DiffPopo:
    my_attr = "diff value"


dict_with_objs = {1: Popo, 2: DiffPopo, 3: ['a', 'b', 'c']}  # The value in a dictionary can be an object

nested_dict = {'key_1': [{'nest_key': ['a', ['b', 'c']]}]}

if __name__ == '__main__':
    print(my_dict['key1'])
    print(fruits_dict['pears'])
    print(dict_with_objs[2].my_attr)
    my_list = dict_with_objs[3]
    print(my_list[2].upper())  # This demonstrates how flexible Python is
    dict_with_objs[1] = 'new value'
    print(dict_with_objs[1])
    print(dict_with_objs.keys())  # Returns all the keys in a dictionary
    print(dict_with_objs.values())  # Returns all the values in a dictionary
    # print(nested_dict['key_1'][0])                      # Returns [{'nest_key': ['a', ['b']]}]
    # print(nested_dict['key_1'][0]['nest_key'][0][0])    # Returns a
    # print(nested_dict['key_1'][0]['nest_key'][1][0])    # Returns b
    # print(nested_dict['key_1'][0]['nest_key'][1][1])    # Returns b
