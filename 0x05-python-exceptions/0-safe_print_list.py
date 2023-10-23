#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for ele in range(x):
            if my_list[ele] == my_list[x - 1]:
                print(my_list[ele])
            else:
                print(my_list[ele], end="")
            count = count + 1
    except IndexError:
        count = 0
        for x in my_list:
            if my_list[-1] == x:
                print(x)
            else:
                print(x, end="")
            count = count + 1
    return count
