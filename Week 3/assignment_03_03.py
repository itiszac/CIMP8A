#! /usr/bin/env python3

sport = "hockey"
city = "Anaheim"
team = ""

if sport == "baseball":
    if city.lower() == "anaheim":
        team = "Angels"
    if city.lower() == "los angeles":
        team = "Dodgers"
elif sport == "hockey":
    if city.lower() == "anaheim":
        team = "Ducks"
    if city.lower() == "los angeles":
        team = "Kings"

print("The " + sport + " team in " + city + " is the " + team)
