#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list"""
    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
