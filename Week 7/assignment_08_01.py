#! /usr/bin/env python3

try:
    # Get a number from the user
    number = int(input("Enter an integer to square: "))

    # Display the number squared
    print("Display the number squared:" + str(number * number))
except ValueError:
    # Display an invalid entry message
    print("You entered an invalid integer")
