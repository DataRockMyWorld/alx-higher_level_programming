#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    if (len(a) > 2) or (len(b) > 2):
        a1, b1 = a[:2]
        a2, b2 = b[:2]
    elif (len(a) == 2) and (len(b) == 2):
        a1, b1 = a
        a2, b2 = b
    else:
        while len(a) < 2:
            a.append(0)
        a1, b1 = a

        while len(b) < 2:
            b.append(0)
        a2, b2 = b

    return a1 + a2, b1 + b2
