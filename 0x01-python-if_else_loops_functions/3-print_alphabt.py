#!/usr/bin/python3
for i in "abcdefghijklmnopqrstuvwxyz":
    if i == 'e' or i == 'q':
        continue
    else:
        print(f"{i.lower()}", end="")
