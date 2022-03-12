#! /usr/bin/env python3
import random


suits = {"Clubs", "Diamonds", "Hearts", "Spades"}
ranks = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop()


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)

    # card value
    def value(self):
        if self.rank == "Ace":
            return 11
        elif self.rank in ["Jack", "Queen", "King"]:
            return 10
        else:
            return int(self.rank)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value()
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def main():
    print("Card Tester")

    # initialize the deck
    deck = Deck()

    # display the first five cards in the deck
    for i in range(5):
        print(f" {str(deck.deck[i])}")
    print()

    # initialize hand
    hand = Hand()

    # deal 3 cards to the hand
    for i in range(3):
        hand.add_card(deck.deal())

    # display the cards in the hand
    print("HAND")
    for card in hand.cards:
        print(f" {str(card)}")
    hand.adjust_for_ace()
    print(f"Points {hand.value}")


if __name__ == "__main__":
    main()
