#!/usr/bin/python3


def element_at(my_list, idx):
    x = len(my_list)
    if not my_list:
        return
    if idx < 0:
        return None
    if idx > x:
        return None
    return my_list[idx]
