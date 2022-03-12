#! /usr/bin/env python3

import deck as d
import db


def print_header():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()


def get_bet(money):
    bet = 0
    while True:
        try:
            bet = float(input("Bet Amounts: "))
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
    print()
    return bet


class Game:
    def __init__(self):
        self.bet = 0.0
        self.db = None
        self.deck = None
        self.player = None
        self.dealer = None

    def __display_hand(self, hand, title):
        print(f"{title.upper()}")
        for card in hand.cards:
            print(f"{str(card)}")
        print()

    def __play_hand(self):
        while True:
            choice = input("Hit or stand? (h/s): ")
            print()
            if choice.lower() == "h":
                self.player.add_card(card=self.deck.deal())
                self.__display_hand(self.player, title="YOUR CARDS:")
                self.player.adjust_for_ace()
                if self.player.value > 21:
                    break
            elif choice.lower() == "s":
                break
            else:
                print("Not a valid choice, please try again.")

    def __results(self):
        if self.player.value > 21:
            msg = "Sorry, you busted! You lose."
            self.db.save(self.db.money - self.bet)
        elif self.player.value == 21 and len(self.player.cards) == 2:
            if self.dealer.value == 21 and len(self.dealer.cards) == 2:
                msg = "Bad luck, you both got a Blackjack! Nobody wins!"
            else:
                msg = "BLACKJACK!"
                self.db.save(self.db.money + self.bet * 1.5)
        elif self.dealer.value == 21 and len(self.dealer.cards) == 2:
            msg = "The dealer got a Blackjack, you lose."
            self.db.save(self.db.money - self.bet)
        elif self.dealer.value > 21:
            msg = "The dealer busted, you win!"
            self.db.save(self.db.money + self.bet)
        elif self.player.value > self.dealer.value:
            msg = "You win!"
            self.db.save(self.db.money + self.bet)
        elif self.player.value < self.dealer.value:
            msg = "You lose."
            self.db.save(self.db.money - self.bet)
        else:
            msg = "Push!"
        print(msg)

    def play(self):
        # init money
        self.db = db.Db("money.txt")

        self.bet = get_bet(self.db.money)

        # init deck
        self.deck = d.Deck()

        # init player's hand
        self.player = d.Hand()

        # init dealer's hand
        self.dealer = d.Hand()

        # deal cards
        self.player.add_card(card=self.deck.deal())
        self.dealer.add_card(card=self.deck.deal())
        self.player.add_card(card=self.deck.deal())

        # display dealer's hand
        self.__display_hand(hand=self.dealer, title="DEALER'S SHOW CARD:")

        # display player's hand
        self.__display_hand(hand=self.player, title="YOUR CARDS:")

        # player's turn
        self.__play_hand()

        # give dealer 2nd card
        self.dealer.add_card(card=self.deck.deal())
        self.dealer.adjust_for_ace()

        if self.player.value <= 21:
            while self.dealer.value < 17:
                self.dealer.add_card(card=self.deck.deal())
                self.dealer.adjust_for_ace()

        # display dealer's hand
        self.__display_hand(hand=self.dealer, title="DEALER'S CARDS:")

        # display points
        print(f"YOUR POINTS:\t\t{self.player.value}")
        print(f"DEALER'S POINTS:\t{self.dealer.value}")
        print()

        # calculate results
        self.__results()

        # display money
        print(f"Money: {round(self.db.money, 2)}\n")
        print()

        if self.db.money < 5:
            print("Sorry, you're out of money. Bye!")
            return False
        return True


def main():
    print_header()

    # initialize game
    game = Game()

    # game loop
    while True:
        again = game.play()
        if not again:
            break

        choice = input("Play again? (y/n): ")
        print()
        if choice.lower() != "y":
            print("Come back soon!")
            break

    print("Bye!")


if __name__ == "__main__":
    main()
