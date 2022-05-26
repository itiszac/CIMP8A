#! /usr/bin/env python3

print("Registration Form\n")

first_name = str(input("First name:\t"))
last_name = str(input("Last name:\t"))
birth_year = int(input("Birth year:\t"))

print(
    f"\nWelcome {first_name} {last_name}!",
    "\nYour registration is complete.",
    f"\nYour temporary password is: {first_name}*{birth_year}",
)
