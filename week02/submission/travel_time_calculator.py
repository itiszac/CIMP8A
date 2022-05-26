#! /usr/bin/env python3

print("Travel Time Calculator\n")

miles = int(input("Enter miles: "))
mph = int(input("Enter miles per hour: "))

print(
    "\nEstimated travel time",
    f"\nHours: {str(int(miles/mph))}",
    f"\nMinutes: {str(int(miles%mph))}",
)
