#! /usr/bin/env python3

import random


def print_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")


def get_results():
    number = random.randint(1, 100)
    result = ""
    if number <= 5:
        result = "blackjack"
    elif 5 < number <= 42:
        result = "win"
    elif 42 < number <= 51:
        result = "push"
    elif 51 < number <= 100:
        result = "lose"
    return result


def calculate_money(money, bet, result):
    if result == "blackjack":
        print("Blackjack!")
        money += bet * 1.5
    elif result == "win":
        print("You won.")
        money += bet
    elif result == "push":
        print("Push.")
    elif result == "lose":
        print("You lost.")
        money -= bet
    return money


def print_results(money):
    print(f"Money: {money:.2f}")


def main():
    print_header()

    starting_money = float(input("Starting money:\t"))
    bet = 0
    while bet != "x":
        bet = input("\nBet amount: ")
        if bet == "x":
            break

        bet = float(bet)
        bet_result = get_results()
        starting_money = calculate_money(
            money=starting_money, bet=bet, result=bet_result
        )
        print_results(money=starting_money)

    print("Bye!")


if __name__ == "__main__":
    main()
