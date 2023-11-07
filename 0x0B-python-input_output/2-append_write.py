#!/usr/bin/python3
"""Module appends string to end of a text file"""


def append_write(filename="", text=""):
    """Fxn appens string to a txt file

    Args: filename, text

    Return: No of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as MyFile:
        return MyFile.write(text)
