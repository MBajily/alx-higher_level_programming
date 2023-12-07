#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for key, value in a_dictionary:
        keys.append(key)

    new_dict = {}
    for key in sorted(keys):
        new_dict[key] = a_dictionary[key]
    return new_dict
