#! /usr/bin/env python3

import random

randomNumber = random.randint(1, 9)
yourGuess = 0
count = 0

while yourGuess != randomNumber and yourGuess != "exit":
    yourGuess = input("Enter a guess between 1 and 9 or exit to end the game ")

    if yourGuess == "exit":
      break

    yourGuess = int(yourGuess)
    count += 1

    if yourGuess < randomNumber:
      print("Too low")
    elif yourGuess > randomNumber:
      print("Too high")
    else:
      print("Right!")
      print("You took only", count, "tries!")
input()
