#!/usr/bin/python
# Filename: using_tuple.py

zoo = ("python", "elephant", "penguin")
print("length of zoo:", len(zoo))

new_zoo = ("monkey", "camel", zoo)
print("length of new_zoo:", len(new_zoo))
print("items in new_zoo:", new_zoo)
print("new_zoo[2]:", new_zoo[2])
print("new_zoo[2][2]:", new_zoo[2][2])
print("number of animals in the new zoo is:", len(new_zoo) - 1 + len(new_zoo[2]))
