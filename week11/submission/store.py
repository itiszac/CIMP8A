#! /usr/bin/env python3

from book import Book


def print_book(books):
    for i in range(len(books)):
        book = books[i]
        print("Title:             {:s}".format(book.title))
        print("Author:            {:s}".format(book.author))
        print("Price:            ${:.2f}".format(book.price))
        print("Discount Percent:  {:.2f}%".format(book.get_discount_percent() * 100))
        print("Discount Amount:  ${:.2f}".format(book.get_discount_amount()))
        print("Discounted Price: ${:.2f}".format(book.get_discounted_price()))
        print()
    print()


def main():
    print("My Book Store")
    print()

    books = (
        Book("The Green Mile", "Stephen King", 19.95, 22),
        Book("Ready Player One", "Ernest Cline", 14.95, 12),
        Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 21.99, 46),
    )

    print_book(books)


if __name__ == "__main__":
    main()
