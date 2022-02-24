#! /usr/bin/env python3


def print_title():
    print("Even or Odd Checker")
    print()


def play_game():
    number = int(input("Enter an integer:  "))
    print("The number is odd." if number&1 else "The number is even.")


def main():
    print_title()
    play_game()


if __name__ == "__main__":
    main()
