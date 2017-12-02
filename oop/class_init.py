#!/usr/bin/python
# Filename: class_init.py


class Person:
    def __init__(self, **name):
        self.name = name["name"]
        print("person init")

    def say(self):
        print("hello, i am a new person called", self.name)

    def dic(d):
        print(d["name"])
        d["name"] = "Jim"
    dic = staticmethod(dic)


m = {"name": "anny"}
Person.dic(m)
print(m)
p = Person(name="anay")
p.say()

