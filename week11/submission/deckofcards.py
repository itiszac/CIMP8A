#! /usr/bin/env python3
import random


class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        self.__value = self.get_value()

    def get_value(self):
        if self.__rank == "Ace":
            value = 11
        elif self.__rank == "Jack" or self.__rank == "Queen" or self.__rank == "King":
            value = 10
        else:
            value = int(self.__rank)
        return value

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit


class Deck:
    def __init__(self):
        self.deck = []

        ranks = [
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        ]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        Card.card = self.deck.pop()
        return Card.card


class Hand:
    def __init__(self):
        self.__cards = []

    def add_card(self, card):
        self.__cards.append(card)

    def get_card(self, index):
        return self.__cards[index]

    def count(self):
        return len(self.__cards)

    def points(self):
        points = 0
        ace_count = 0
        for card in self.__cards:
            if card.get_rank() == "Ace":
                ace_count += 1
            points += card.get_value()

        if ace_count > 0 and points > 21:
            points -= 10 * ace_count
        if ace_count > 1 and points <= 11:
            points += 10
        return points


def main():
    print("Cards - Tester")
    print()

    deck = Deck()
    deck.shuffle()

    print("HAND")
    hand = Hand()
    for i in range(3):
        hand.add_card(deck.deal_card())

    for i in range(hand.count()):
        card = hand.get_card(i)
        print(card.get_rank() + " of " + card.get_suit())

    print("Hand points:", hand.points())


if __name__ == "__main__":
    main()
