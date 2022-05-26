#! /usr/bin/env python3
"""
This module contains functions for converting
temperatures between degrees Fahrenheit
and degrees Celsius
"""

def to_celsius(fahrenheit):
    """
    This converts degrees Fahrenheit to Celsius
    :param fahrenheit: This is the degrees Fahrenheit to convert
    :return: The converted Celsius value
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def to_fahrenheit(celsius):
    """
    This converts degrees Celsius to Fahrenheit
    :param celsius: This is the degrees Celsius to convert
    :return: The converted Fahrenheit value
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# the main() function is used to test the conversion functions
# this code isn't run if this isn't the main module
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")


# if this module is the main module, call the main()
# function to test the conversion functions
if __name__ == "__main__":
    main()
