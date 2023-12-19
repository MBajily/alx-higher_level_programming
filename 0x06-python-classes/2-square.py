#!/usr/bin/python3
"""Square module"""


class Square:
    """an empty class Square that defines a square."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: square size.
        """
        if str(size).isdigit():
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

        else:
            raise TypeError("size must be an integer")
