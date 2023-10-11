#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0

    core = []
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and roman_string[i : i + 2] in dic:
            core.append(dic[roman_string[i : i + 2]])
        else:
            core.append(dic[roman_string[i]])

    return sum(core)
