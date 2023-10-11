#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new = list(my_list)
    for indx, v in enumerate(new):
        if v == search:
            new[indx] = replace
    return new
