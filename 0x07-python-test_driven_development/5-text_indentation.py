#!/usr/bin/python3
# 5-text_indentation.py
"""this for Defines a text-indentation function."""


def text_indentation(text):
    """for Print text with two new line after  '.', '?', and ':'.

    Args:
        text (string):for  The text to print.
    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
