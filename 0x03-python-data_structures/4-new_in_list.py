#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy = []
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    for w in my_list:
        if my_list[idx] == w:
            my_list[idx] = element
            copy.append(my_list[idx])
        else:
            copy.append(w)
    return copy
