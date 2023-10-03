#!/usr/bin/python3
def islower(c):
    if c.isnumeric():
        return False
    elif ord(c) == ord(c.lower()):
        return True
    else:
        return False
