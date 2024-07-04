#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ find the peak number with the shortest algorithm"""
    n = len(list_of_integers)

    # Check if the list is empty
    if n == 0 or list_of_integers is None:
        return None

    # Check if the list has only one element
    #if n == 1:
    #    return list_of_integers[0]

    # Binary search to find the peak
    low = 0
    high = n
    mid = int(((high - low) // 2) + low)

    if high == 1:
        return list_of_integers[0]

    if high == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1]\
            and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
