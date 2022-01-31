#! /usr/bin/env python3

# display the header
print("Change Calculator")
print()

choice = "y"
while choice.lower() == "y":
    # get the input from user
    cents = int(input("Enter number of cents (0-99): "))
    print()

    # display the results
    print(
        f"Quarters:\t{cents // 25}\n"
        + f"Dimes:\t\t{(cents % 25) // 10}\n"
        + f"Nickels:\t{(cents % 25) % 10 // 5}\n"
        + f"Pennies:\t{(cents % 25) % 10 % 5}\n"
    )

    # see if the user wants to do it again
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
