#!/usr/bin/python3

"""
 function that prints a text with 2 new lines after each of these characters:
 
 ., ? and :
 
"""


def text_indentation(text):
    """
    prints two new lines after characters (".", "?" and ":")

    Argument : Text which is a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = []
    lines = text.split("\n")

    for line in lines:
        new_line = []
        for ch in line:
            new_line.append(ch)
            if ch in (".", "?", ":"):
                new_line.append("\n\n")

        new_text.append("".join(new_line))

    result = "\n".join(new_text)
    print(result)
