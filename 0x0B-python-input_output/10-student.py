#!/usr/bin/python3
"""this for Defines a class Student."""


class Student:
    """for Represent a student."""

    def __init__(self, first_name, last_name, age):
        """this for Initialize a new Student.

        Args:
            first_name (str): for first name of the student.
            last_name (str): for last name of the student.
            age (int): for  age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """for Get a dictionary representation of the Student.

        If attrs is a list of str, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) for  attr to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
