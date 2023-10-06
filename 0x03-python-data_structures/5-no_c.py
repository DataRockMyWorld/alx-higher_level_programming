#!/usr/bin/python3


def no_c(my_string):
    list = []
    for w in my_string:
        if w == "c" or w == "C":
            continue
        else:
            list.append(w)

    return "".join(list)
