#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sort = dict(sorted(a_dictionary.items()))

    for k, v in sort.items():
        print(k, v, sep=": ")
