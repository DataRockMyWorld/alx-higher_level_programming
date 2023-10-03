#!/usr/bin/python3
def uppercase(str):
    upper_c = ""
    for i in str:
        if "a" <= i <= "z":
            upper_c += chr(ord(i) - ord("a") + ord("A"))
        else:
            upper_c += i
        
    print("{}".format(upper_c))
