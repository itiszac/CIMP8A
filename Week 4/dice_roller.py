#! /usr/bin/env python3

import random


def print_title():
    print("Dice Roller")
    print()


def play_game():
    die_one = random.randint(1, 6)
    print("Die 1:", str(die_one))

    die_two = random.randint(1, 6)
    print("Die 2:", str(die_two))

    total = die_one + die_two
    print("Total:", str(total))

    if total == 2:
        print("Snake eyes!")
    elif total == 12:
        print("Boxcars!")


def main():
    print_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        print()
        again = input("Roll again? (y/n): ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
