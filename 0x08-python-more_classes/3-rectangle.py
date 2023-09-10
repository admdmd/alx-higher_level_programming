#!/usr/bin/python3

"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    def __init__(i, width=0, height=0):
        """Initialiazes the rectangle"""
        i.width = width
        i.height = height

    @property
    def width(i):
        """Returns the width of rectangle"""
        return (i.__width)

    @width.setter
    def width(i, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        i.__width = value

    @property
    def height(i):
        """Returns the height of rectangle"""
        return (i.__height)

    @height.setter
    def height(i, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        i.__height = value

    def area(i):
        """Returns the area of the rectangle"""
        return i.width * i.height

    def perimeter(i):
        """Returns the perimeter of the rectangle"""
        if not i.width or not i.height:
            return 0
        return 2 * (i.height + i.width)

    def __str__(i):
        """Returns a string rep of the rectangle"""
        if not i.width or not i.height:
            return ""
        return (("#" * i.width + "\n") * i.height)[:-1]
