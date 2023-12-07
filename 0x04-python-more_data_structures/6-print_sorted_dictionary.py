#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())

    new_dict = {}
    for key in sorted(keys):
        print(f'{new_dict[key]} = {a_dictionary[key]}')
