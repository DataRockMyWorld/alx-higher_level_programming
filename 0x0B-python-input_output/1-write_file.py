#!/usr/bin/python3
"""Module has a function that writes string to txt file"""


def write_file(filename="", text=""):
    """Fxn writes string to a txt file and
    returns no of characters printed

    Args: filename
           text
    """
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        return MyFile.write(text)
