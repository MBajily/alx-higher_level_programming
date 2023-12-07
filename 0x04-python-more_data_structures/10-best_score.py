#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = min(a_dictionary.values()) - 1

    for key, value in a_dictionary.items():
        if value > best_score:
            best_key = key
            best_score = value

    return best_key
