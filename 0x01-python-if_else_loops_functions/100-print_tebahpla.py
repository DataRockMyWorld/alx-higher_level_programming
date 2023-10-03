#!/usr/bin/python3
start = 0
lower = 90

for value in range(1, 27):
    if value % 2 == 0:
        start = lower
    else:
        start = 123 - value

    lower -= 1
    print("{}".format(chr(start)), end="")
