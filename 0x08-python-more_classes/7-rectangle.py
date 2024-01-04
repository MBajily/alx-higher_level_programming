#!/usr/bin/python3
"""
Create a class called Rectangle
"""


class Rectangle:
    """Represent of the rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @width.setter
    def width(self, value):
        """Set a new value to the private width attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """Return the area of the rectanle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Draw the rectangle using #"""
        string = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += self.print_symbol
                if i != (self.__height - 1):
                    string += '\n'
        return string

    def __repr__(self):
        """Return the represntation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Return a message when the object is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
