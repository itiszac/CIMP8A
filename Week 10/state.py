#! /usr/bin/env python3


def display_menu():
    print("COMMAND MENU")
    print("view - View State")
    print("add - Add a State")
    print("del - Delete a State")
    print("exit - Exit the program")
    print()


def display_codes(states):
    codes = list(states.keys())
    codes.sort()
    codes_line = "State codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)


def view(states):
    display_codes(states)
    code = input("Enter state code: ")
    code = code.upper()
    if code in states:
        name = states[code]
        print("State name: " + name + ".\n")
    else:
        print("There is no state with that code.\n")


def add(states):
    code = input("Enter state code: ")
    code = code.upper()
    if code in states:
        name = states[code]
        print(name + " is already using this code.\n")
    else:
        name = input("Enter state name: ")
        name = name.title()
        states[code] = name
        print(name + " was added.\n")


def delete(states):
    code = input("Enter state code: ")
    code = code.upper()
    if code in states:
        name = states[code]
        del states[code]
        print(name + " was deleted.\n")
    else:
        print("There is no state with that code.\n")


def main():
    states = {"CA": "California", "AZ": "Arizona"}
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(states)
        elif command == "add":
            add(states)
        elif command == "del":
            delete(states)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
