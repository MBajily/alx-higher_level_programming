#!/usr/bin/python3
"""Square module"""


class Square:
    """return a square size."""

    def __init__(self, size=0):
        """Constructor

        Args:
            size (int): square size.
        """
        self.size = size


    @property
    def size(self):
        """Get current size of the square."""
        return self.__size
    

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if int(value) < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = value

    
    def area(self):
        """Area

        Returns:
            size: the square's size.
        """
        return self.__size * self.__size
