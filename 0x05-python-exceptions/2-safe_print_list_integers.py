#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for ele in range(x):
        try:
            print("{:d}".format(my_list[ele]), end="")
            count = count + 1
        except (ValueError, TypeError):
            pass
    print()
    return count
