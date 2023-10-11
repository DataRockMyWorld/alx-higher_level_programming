#!/usr/bin/python3


def weight_average(my_list=[]):
    if not list:
        return 0
    mul = 0
    sum = 0
    for w in my_list:
        score, weight = w
        mul = mul + (score * weight)
        sum += weight
    return mul / sum
