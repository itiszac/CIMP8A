#! /usr/bin/env python3


def display_header():
    print("Prime Number Checker")
    print()


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def get_number():
    while True:
        try:
            number = int(input("Please enter an integer between 1 and 5000: "))
            if 1 <= number <= 5000:
                return number
            else:
                print("Number must be between 1 and 5000.")
        except Exception as e:
            print(e)


def display_results(number):
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        factors = get_factors(number)
        print(f"It has {len(factors)} factors: {' '.join(map(str, factors))}")
    print()


def main():
    display_header()

    choice = "y"
    while choice.lower() == "y":
        print()
        number = get_number()
        display_results(number=number)

        choice = input("Try again? (y/n): ")

    print("Bye!")


if __name__ == "__main__":
    main()
