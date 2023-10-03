#!/usr/bin/python3
def remove_char_at(str, n):
    box = list(str)

    if n > len(box) or (n < 0):
        return str
    
    elif n <= len(box):
        del box[n]
        return "".join(box)
