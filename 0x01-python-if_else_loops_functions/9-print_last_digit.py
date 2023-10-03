#!/usr/bin/python3
def print_last_digit(number):
    y = int(number)
    y = abs(y)
    last = y % 10
    if y > 0:
        print(f"{last}", end="")
        return last
    elif y < 0:
        print(f"{last}", end="")
        return last
    else:
        print("0", end="")
        return 0
