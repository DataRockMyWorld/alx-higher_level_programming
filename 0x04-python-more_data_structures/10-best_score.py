#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    val = []
    for k, v in a_dictionary.items():
        val.append(v)
    m = max(val)

    for a, b in a_dictionary.items():
        if b == m:
            return a
    
