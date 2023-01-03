#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is negative".format(number))
elif number == 0:
    print(f"{number} is zero")
else:
    print(number, "is positive")
