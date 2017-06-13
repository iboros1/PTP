# !/usr/bin/env python3


# P1. Given a dictionary, swap keys <-> values. The program should use some custom logic to check if the swap is possible, but without using try..
# except constructs or the __hash__() function.
# Example:
# Input: {'a': 123, 'b': 456}
# Output: {123: 'a', 456: 'b'}
# ------------------------------------------------
# Input: {'a': (1, 2, [3])}
# Output: Swap is not possible


my_dict = {'a': 123, 'b': 456, 'c': 123}
new_dict = {}


def swap_keys():
    for key, value in my_dict.items():
        if type(value) == int or type(value) == str:
            if value not in new_dict.keys():
                new_dict[value] = key
            elif value in new_dict.keys():
                new_dict[value] += key
        else:
            return "Swap is not possible"
    return new_dict

print(swap_keys())

