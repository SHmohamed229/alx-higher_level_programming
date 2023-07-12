#!/usr/bin/python3
"""this for Defines a file-writing function."""


def write_file(filename="", text=""):
    """for Write a string to a UTF8 text file.

    Args:
        filename (str): for name of the file to write.
        text (str): for text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
