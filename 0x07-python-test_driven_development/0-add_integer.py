#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Raises:
        TypeError: If a or b are not float or integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
