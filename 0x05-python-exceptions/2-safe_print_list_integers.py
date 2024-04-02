#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for i in range(0, x):
        try:
            total += 1
            print('{:d}'.format(my_list[i]), end='')
        except (TypeError, ValueError):
            total -= 1
            continue
    print()
    return total
