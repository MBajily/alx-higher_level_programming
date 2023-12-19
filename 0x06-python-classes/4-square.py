#!/usr/bin/python3
"""Square module"""


class Square:
    """an empty class Square that defines a square."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: square size.

        Raises:
            ValueError: "size must be >= 0"
            TypeErro: ("size must be an integer"
        """
        if isinstance(size, int):
            if int(size) < 0:
                raise ValueError("size must be >= 0")

        else:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """Area

        Returns:
            size: the square's size.
        """
        return self.__size * self.__size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if int(value) < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size
