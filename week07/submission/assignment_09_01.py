#! /usr/bin/env python3

import math as m

num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))

print()

# The power function
print(str(num1) + " to the power of " + str(num2) + " is " + str(m.pow(num1, num2)))

# The square root function
print("The square root of " + str(num1) + " is " + str(m.sqrt(num1)))

# The ceiling function
print(
    "The nearest integer (rounded up) to "
    + str(num1 / num2)
    + " is "
    + str(m.ceil(num1 / num2))
)

# The floor function
print(
    "The nearest integer (rounded down) to "
    + str(num1 / num2)
    + " is "
    + str(m.floor(num1 / num2))
)

# Calculate the area of a circle using the pi function
print(
    "The area of the circle with radius " + str(num1) + " is: " + str(m.pi * num1**2)
)
