#!/usr/bin/python3
def best_score(a_dictionary):
    sorted_values = reversed(a_dictionary.values())
    for key, value in dictionary.items():
        if value == max(sorted_values):
            return key
    return None
