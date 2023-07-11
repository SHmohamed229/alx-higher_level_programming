#!/usr/bin/python3
"""this for Define a class MyInt that inherits from int."""


class MyInt(int):
    """for Invert int operators == and !=."""

    def __eq__(self, value):
        """for Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """for Override != operator with == behavior."""
        return self.real == value
