#! /usr/bin/env python3
import random

DIE_SIZE = 6


class Die:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = 0

    def roll(self):
        self.__value = random.randint(1, self.__sides)
        print("Die:", self.__value)

    def get_value(self):
        return self.__value


class Game:
    def __init__(self):
        self.__turn = 1
        self.__score = 0
        self.__score_this_turn = 0
        self.__is_turn_over = False
        self.__is_game_over = False
        self.__die = Die(DIE_SIZE)

    def play(self):
        while not self.__is_game_over:
            self.__play_turn()

    def __reset_turn(self):
        self.__is_turn_over = False
        self.__score_this_turn = 0

    def __play_turn(self):
        print("TURN", self.__turn)
        self.__reset_turn()
        while not self.__is_turn_over:
            choice = input("Roll or Hold? (r/h): ")
            if choice.lower() == "r":
                self.__roll()
            elif choice.lower() == "h":
                self.__hold()
            else:
                print("Invalid choice. Try again.")

    def __roll(self):
        self.__die.roll()
        if self.__die.get_value() == 1:
            self.__score_this_turn = 0
            self.__turn += 1
            self.__is_turn_over = True
            print("Turn over. No scores.\n")
        else:
            self.__score_this_turn += self.__die.get_value()

    def __hold(self):
        self.__score += self.__score_this_turn
        self.__is_turn_over = True
        print("Score for turn:", self.__score_this_turn)
        print("Total score:", self.__score, "\n")
        if self.__score >= 20:
            self.__is_game_over = True
            print("You finished in", self.__turn, "turns!")
        else:
            self.__turn += 1


def print_header():
    print("Let's Player PIG!")
    print()
    print("* See how many turn it takes you to get to 20.")
    print("* Turn ends when you hold or roll a 1.")
    print("* If you roll a 1, you lose all points for the turn.")
    print("* If you hold, you save all points for the turn.")
    print()


def main():
    print_header()

    again = "y"
    while again.lower() == "y":
      # initialize game
      game = Game()
      game.play()

      again = input("Play again? (y/n): ")
      print()


if __name__ == "__main__":
    main()
