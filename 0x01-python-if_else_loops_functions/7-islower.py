#!/usr/bin/python3
def islower(c):
    if c.isalpha():
        if ord(c) == ord(c.lower()):
            return True
        else:
            return False
    else:
        return False
