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


def get_starting_money():
    money = 0.0
    while True:
        try:
            money = float(input("Starting money:\t"))
            if 5 <= money <= 10000:
                break
            print("Invalid amount. Must be between 5 and 10,000. Please try again.")
        except Exception as e:
            print(e)
    return money


def get_bet(money):
    bet = 0
    print()
    while True:
        try:
            bet = input("Bet Amounts: ")
            if bet == "x":
                break
            bet = float(bet)
            if bet < 5:
                print("The minimum bet is 5. Please try again.")
            elif bet > 1000:
                print("The maximum bet is 1000. Please try again.")
            elif bet > money:
                print("You don't have enough to cover that bet. Please try again.")
            else:
                break
        except Exception as e:
            print(e)
    return bet


def main():
    print_header()

    money = get_starting_money()

    bet = 0
    while bet != "x":
        bet = get_bet(money)
        if bet == "x":
            break
        bet_result = get_results()
        money = calculate_money(money=money, bet=bet, result=bet_result)
        print_results(money=money)

    print("Bye!")


if __name__ == "__main__":
    main()
