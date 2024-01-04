#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Find and return the max integer in a list
    """
    if (len(list) == 0):
        return None

    r = list[0]

    i = 1

    while (i < len(list)):
        if (list[i] > r):
            r = list[i]
        i += 1

    return r
