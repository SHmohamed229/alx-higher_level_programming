#!/usr/bin/python3
"""this for Define a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """for Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """for Intialize a new Rectangle.

        Args:
            width (int): for width of the new Rectangle.
            height (int): for height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
