#!/usr/bin/python
# Filename: objvar.py


class Robot:
    # """Represent a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("(Initialize {0})".format(self.name))
        Robot.population += 1

    def __del__(self):
        """I am dying."""

        Robot.population -= 1
        if Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("There are still {0:d} robots working.".format(Robot.population))

    def sayHi(self):
        """Greeting by the robot."""

        print("Greetings, my master call me {0}.".format(self.name))

    def howMany():
        """Prints the current population"""
        print("We have {0:d} robots.".format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot("R2-D2")
droid1.sayHi()

droid2 = Robot("C-3P0")
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

del droid1
del droid2

Robot.howMany()