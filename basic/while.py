#! /usr/bin/python
# Filename: while.py

number = 23
running = True

while running:
    guess = int(input("Engter an integer: "))
    if guess == number:
        print("Congratulations, you guess it!")
        running = False
    elif guess < number:
        print("No, it is a little higher.")
    else:
        print("No, it it a little lower.")
else:
    print("the while loop is over.")
print("Done!")
