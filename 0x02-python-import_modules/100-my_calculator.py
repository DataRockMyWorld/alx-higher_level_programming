#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operator = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == operator[0]:
        print(f"{a} + {b} = {add(a, b)}")
    elif sys.argv[2] == operator[1]:
        print(f"{a} - {b} = {sub(a, b)}")
    elif sys.argv[2] == operator[2]:
        print(f"{a} * {b} = {mul(a, b)}")
    else:
        print(f"{a} / {b} = {div(a, b)}")
