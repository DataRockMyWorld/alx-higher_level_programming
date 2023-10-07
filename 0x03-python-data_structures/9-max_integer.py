#!/usr/bin/python3


def max_integer(my_list=[]):
    max = my_list[0]

    for w in my_list:
        if w > max:
            max = w
        else:
            continue
    return max
