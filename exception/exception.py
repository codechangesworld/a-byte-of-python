#!/usr/bin/python
# Filename: exception.py


class ShotInputException(Exception):
    """A user-defined exception class"""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("Enter something --> ")
    if len(text) < 3:
        raise ShotInputException(len(text), 3)
except EOFError:
    print("EOF Error occurs!")
except ShotInputException as ex:
    print("ShotInputException The input was {0} long, excepted "
          "at least {1}".format(ex.length, ex.atleast))
else:
    print("No excetion was raised.")
finally:
    print("Here is finally block.")
