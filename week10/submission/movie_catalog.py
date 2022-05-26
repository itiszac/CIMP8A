#! /usr/bin/env python3

# display the full menu list
def display_menu():
    print("The Movie Catalog program")
    print()
    print("Menu")
    print("show - Show Movie Info")
    print("add - Add a Movie")
    print("edit - Edit Movie Info")
    print("del - Delete a Movie")
    print("exit - Exit the program")


# show an individual movie
def show_movie(movie_catalog):
    title = input("Enter the title for the movie: ")
    if title in movie_catalog:
        movie = movie_catalog[title]
        print("Title:        ", title)
        print("Lead Actor:   ", movie["actor"])
        print("Release Year: ", movie["year"])
    else:
        print("Sorry,", title, "does not exist in the catalog.")


# add or edit a movie in the catalog
def add_edit_movie(movie_catalog, mode):
    title = input("Enter the title for the movie: ")
    if mode == "add" and title in movie_catalog:
        print(title, "already exists in the catalog.")
        response = input("Would you like to edit it? (y/n): ").lower()
        if response != "y":
            return
    elif mode == "edit" and title not in movie_catalog:
        print(title, "does not exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if response != "y":
            return

    # get movie data and create a dictionary for the data
    actor = input("Enter the actor name: ")
    year = input("Enter the release year: ")
    movie = {"actor": actor, "year": year}

    # add the movie data to the catalog using title as key
    movie_catalog[title] = movie


# delete a movie from catalog
def delete_movie(movie_catalog):
    title = input("Enter the title for the movie: ")
    if title in movie_catalog:
        del movie_catalog[title]
        print(title, "removed from the catalog.")
    else:
        print(title, "does not exist in the movie catalog.")


def main():
    movie_catalog = {
        "Big": {"actor": "Tom Hanks", "year": "1988"},
        "Toy Story": {"actor": "Tim Allen", "year": "1994"},
        "Man on Fire": {"actor": "Denzel Washington", "year": "2004"},
    }
    display_menu()
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_movie(movie_catalog)
        elif command == "add":
            add_edit_movie(movie_catalog, mode="add")
        elif command == "edit":
            add_edit_movie(movie_catalog, mode="edit")
        elif command == "del":
            delete_movie(movie_catalog)
        elif command == "exit":
            print("That's all folks!")
            break
        else:
            print("Unknown command.  Please try again.")


if __name__ == "__main__":
    main()
