#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if not my_list or search not in my_list:
        return

    new = list(my_list)
    for indx, v in enumerate(new):
        if v == search:
            new[indx] = replace
    return new
