#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = [0, 1, 1]
    if length <= 3:
        print(my_list[0:length])
    else:
        for i in range(3, length):
            my_list.append(my_list[i-1]+my_list[i-2])

        print(my_list[0:length])
    