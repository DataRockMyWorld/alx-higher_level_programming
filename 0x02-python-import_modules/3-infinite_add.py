#!/usr/bin/python3
from add_0 import add
from sys import argv

if __name__ == "__main__":
    total = 0

    if len(argv) == 1:
        print("0")
    else:
        for arg in argv[1:]:
            arg = int(arg)
            total = add(total, arg)
        print(f"{total}")
