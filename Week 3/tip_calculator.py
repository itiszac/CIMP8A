#! /usr/bin/env python3

# display the header
print("Tip Calculator")
print()

# get the input from user
meal_cost = float(input("Cost of meal:\t"))
print()

# display the results
tip_percent = 0.15
tip_amount = round(meal_cost * tip_percent, 2)
total_amount = round(meal_cost + tip_amount, 2)
print(f"15%\nTip amount:\t{tip_amount}\nTotal amount:\t{total_amount}\n")

tip_percent = 0.20
tip_amount = round(meal_cost * tip_percent, 2)
total_amount = round(meal_cost + tip_amount, 2)
print(f"20%\nTip amount:\t{tip_amount}\nTotal amount:\t{total_amount}\n")

tip_percent = 0.25
tip_amount = round(meal_cost * tip_percent, 2)
total_amount = round(meal_cost + tip_amount, 2)
print(f"25%\nTip amount:\t{tip_amount}\nTotal amount:\t{total_amount}\n")
