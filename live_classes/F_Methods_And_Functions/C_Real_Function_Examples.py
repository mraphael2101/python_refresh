def check_even_list(num_list):
    """
    Function returns True if any value in the list is even
    :param num_list:
    :return: boolean
    """
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False


print(check_even_list([1, 3, 5, 7]))
print(check_even_list([1, 3, 5, 7, 2]))


def get_even_no_list(num_list: object) -> []:
    """
    Function to return a list of even numbers in a list
    :param num_list:
    :return: even_numbers_list
    """
    even_numbers_list = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers_list.append(number)
        else:
            pass
    return even_numbers_list


print(get_even_no_list([1, 3, 5, 7, 2, 4, 6]))
