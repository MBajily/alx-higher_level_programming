#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    # Get the length of the list
    n = len(list_of_integers)

    # Check if the list is empty
    if n == 0:
        return None

    # Check if the list has only one element
    if n == 1:
        return list_of_integers[0]

    # Binary search to find the peak
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        current = list_of_integers[mid]

        # Check if the current element is a peak
        if (mid == 0 or current >= list_of_integers[mid - 1])\
                and (mid == n - 1\
                or current >= list_of_integers[mid + 1]):
                    return current

        # If the current element is not a peak, move to the left or right
        if mid > 0 and list_of_integers[mid - 1] > current:
            high = mid - 1
        else:
            low = mid + 1
    return None
