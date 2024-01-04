#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """Print a square using '#'.

    Args:
        size (int): size(height) x size(width)
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size)
            print("#", end="")
        print("")
