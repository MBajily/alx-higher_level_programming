#!/usr/bin/python3
"""Square module"""


class Square:
    """return a square size."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size (int): square size.
            position (int, int): The position.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set current size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if int(value) < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if ((len(value) != 2) or (not isinstance(value, tuple)) or
                (not all(isinstance(num, int) for num in value)) or
                (not all(num >= 0 for num in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__posistion = value

    def area(self):
        """Return square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
