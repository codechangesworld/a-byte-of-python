#!/usr/bin/python
# Filename: func_docstring.py


def printMax(x, y):
    '''
    Prints the maximum of two numbers.

    The two numbers must be integers.
    :param x:
    :param y:
    :return:
    '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum.")
    else:
        print(y, "is maximum")


print(printMax.__doc__)
printMax(3, 5)
