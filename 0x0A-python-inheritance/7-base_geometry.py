#!/usr/bin/python3
"""this class for Define a base geometry class BaseGeometry."""


class BaseGeometry:
    """for Reprsent base geometry."""

    def area(self):
        """for Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """for Validate a parameter as an int.

        Args:
            name (str): for The name of the parameter.
            value (int): for The parameter to validate.
        Raises:
            TypeError: for If value is not an int.
            ValueError: for If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
