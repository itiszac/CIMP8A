#! /usr/bin/env python3


def print_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit\n")


def calculate_money(money, bet, bet_type):
    if bet_type.lower() == "b":
        money += bet * 1.5
    elif bet_type.lower() == "w":
        money += bet
    elif bet_type.lower() == "p":
        pass
    elif bet_type.lower() == "l":
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
        bet_type = input("Blackjack, win, push, or lose? (b/w/p/l): ")
        starting_money = calculate_money(
            money=starting_money, bet=bet, bet_type=bet_type
        )
        print_results(money=starting_money)

    print("Bye!")


if __name__ == "__main__":
    main()
