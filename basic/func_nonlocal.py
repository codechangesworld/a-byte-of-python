#!/usr/bin/python
# Filename: func_nonlocal.py

x = 10


def func_outer():
    x = 3
    print("local x :", x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print("change nonlocal x to:", x)


print("global:", x)
func_outer()
print("global:", x)
