#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list = []

    for w in my_list:
        if w % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
