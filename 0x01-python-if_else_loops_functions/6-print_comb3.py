#!/usr/bin/python3
i = 0
while (i < 10):
    j = 0
    while (j < 10):
        if (i < j) and (i != j):
            print(f"{i}{j},", end=" ")
        elif (i + j) == 17:
            print(f"{i}{j}")
        j = j + 1
    i = i + 1
print()
