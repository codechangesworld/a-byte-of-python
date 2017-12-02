#!/usr/bin/python
# Filename: func_var_args.py


def total(initial=5, *numberlist, **keymap):
    count = initial
    for i in numberlist:
        count += i
    for key in keymap:
        count += keymap[key]
    return count


print("total count is", total(10, 1, 2, 3, veg=50, fru=80))
