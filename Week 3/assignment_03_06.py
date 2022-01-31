#! /usr/bin/env python3

print("Enter 'exit' when you\'re done.\n")
while True:
    data = input("Enter an integer to sqaure: ")
    if data == "exit":
        break
    i = int(data)
    print(i, "squared is", i * i, "\n")
print("The program has ended")
