#!/usr/bin/python3
"""
Create a class called Rectangle
"""


class Rectangle:
    """Represent of the rectangle class"""
    def __int__(self, width=0, height=0):
        """Init rectangle class"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """getiing private height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting a new value to the private height attr"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """Getting the private height value"""
        return self.__width

    @height.setter
    def width(self, value):
        """Set a new value to the private width attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value
