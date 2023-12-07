#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, v in a_dictionary.items():
        if v == value:
            del new_dict[key]
    return new_dict
