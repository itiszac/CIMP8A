#! /usr/bin/env python3


def display_header():
    print("The Total Calculator Program")
    print()


def get_price():
    try:
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid decimal number. Please try again.")
        price = get_price()
    return price


def get_quantity():
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid integer. Please try again.")
        quantity = get_quantity()
    return quantity


def display_total(price, quantity):
    total = price * quantity
    print(f"\nPRICE:\t\t{price:.2f}")
    print(f"QUANTITY:\t{quantity}")
    print(f"TOTAL:\t\t{total:.2f}\n")


def main():
    display_header()

    price = get_price()
    quantity = get_quantity()

    display_total(price, quantity)


if __name__ == "__main__":
    main()
