#! /usr/bin/env python3


def print_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")


def print_results(starting_money, bet):
  print("\nENDING MONEY FOR A...")
  print(f"Blackjack:\t{starting_money + (bet * 1.5):.2f}")
  print(f"Win:\t\t{starting_money + bet:.2f}")
  print(f"Push:\t\t{starting_money:.2f}")
  print(f"Lose:\t\t{starting_money - bet:.2f}")


def main():
    print_header()

    starting_money = int(input("Starting money:\t"))
    bet = int(input("Bet amount:\t"))

    print_results(starting_money, bet)


if __name__ == "__main__":
    main()
