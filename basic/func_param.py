#!/usr/bin/python
# Filename: func_param.py


def printMax(a, b):
    print("{0} and {1} ".format(a, b))
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to ", b)
    else:
        print(b, "is maximum")


printMax(3, 4)
x = 5
y = 8
printMax(x, y)
