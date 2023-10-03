#!/usr/bin/python3
i = 0
while i < 9:
    j = 0
    while j < 10:
        if (i < j) and (i != j):
            print("{}{},".format(i, j), end=" ")
        if (i + j) == 17:
            print("{}{}".format(i, j))
        j = j + 1
    i = i + 1

