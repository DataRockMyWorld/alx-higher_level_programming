#!/usr/bin/python3
def islower(c):
    if c.isnumeric():
        return False
    elif c == c.lower():
        return True
    else:
        return False
