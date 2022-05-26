#! /usr/bin/env python3
import requests
import textwrap


def display_title():
    """
    This method will display the title screen
    """
    print("My Recipe Program")
    print()


def display_menu():
    """
    This method will display the menu
    """
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all Areas")
    print("6 - Search Meals by Area")
    print("7 - Menu")
    print("0 - Exit the application")
    print()


def verify_category(category):
    """
    This method will verify that the category is valid
    """
    categories = requests.get_categories()
    for c in categories:
        if c.get_name().lower() == category.lower():
            return True
    return False


def verify_area(area):
    """
    This method will verify that the area is valid
    """
    areas = requests.get_areas()
    for a in areas:
        if a.get_name().lower() == area.lower():
            return True
    return False


def print_recipe(recipe):
    """
    This method will print the recipe
    """
    print("Recipe:  " + recipe.get_meal_name())
    print()
    instructions = recipe.get_meal_instructions()

    print(
        "Instructions:\n" + textwrap.fill(instructions, width=80)
    )  # Wrap the instructions
    print()
    print("Ingredients:")
    print("{:<15} {:<15}".format("Measure", "Ingredient"))
    print("-" * 80)
    for i in recipe.get_meal_ingredients():
        print("{:<15} {:<15}".format(i.get("measure"), i.get("ingredient")))
    print()


def print_meals(title, meals):
    """
    This method will print the meals
    """
    print(title, "MEALS")
    for m in meals:
        print("  " + m.get_meal_name())
    print()


def get_menu_choice():
    """
    This method will get the user's menu choice
    """
    choice = input("What would you like to do? ")
    print()
    # ensure that the choice is an integer
    try:
        # validate the choice
        choice = int(choice)
        if choice < 0 or choice > 7:
            print("Invalid choice")
            choice = None
    except ValueError:
        print("Invalid choice. Please enter a valid integer.")
        choice = None
    return choice


def display_menu_item_by_choice(choice):
    """
    This method will display the menu item based on the choice
    """
    if choice == 1:
        display_categories()
    elif choice == 2:
        category = input("Enter a category: ")
        display_meals_by_category(category)
    elif choice == 3:
        meal_name = input("Enter a meal name: ")
        print()
        display_recipe_by_name(meal_name)
    elif choice == 4:
        display_random_meal()
    elif choice == 5:
        display_areas()
    elif choice == 6:
        area = input("Enter an area: ")
        display_meals_by_area(area)
    elif choice == 7:
        display_menu()
    elif choice == 0:
        print("Thank you for dining with us!")
        exit(1)


def display_categories():
    """
    This method will fetch all of the categories and display them on screen
    """
    categories = requests.get_categories()
    if categories is None:
        print("Technical difficulties, please try again later.")
    else:
        print("CATEGORIES")
        for c in categories:
            print("  " + c.get_name())
        print()


def display_meals_by_category(category):
    """
    This method get the meal list for that category if it is valid
    """
    if verify_category(category):
        meals = requests.get_meals_by_category(category)
        if meals is None:
            print("Technical difficulties, please try again later.")
        else:
            print_meals(title=category.upper(), meals=meals)
    else:
        print("Invalid category")


def display_recipe_by_name(name):
    """
    This method will prompt the user for a meal name
    and get the meal if it is valid
    """
    recipe = requests.get_recipe_by_name(name)
    if recipe is None:
        print("Technical difficulties, please try again later.")
    else:
        print_recipe(recipe)


def display_random_meal():
    """
    This method will get a random meal and display it on the screen
    """
    recipe = requests.get_random_recipe()
    if recipe is None:
        print("Technical difficulties, please try again later.")
    else:
        print("A random meal was selected just for you!\n")
        print_recipe(recipe)


def display_areas():
    """
    This method will fetch all of the areas and display them on screen
    """
    areas = requests.get_areas()

    if areas is None:
        print("Technical difficulties, please try again later.")
    else:
        print("AREAS:")
        for a in areas:
            print("  " + a.get_name())
        print()


def display_meals_by_area(area):
    """
    This method get the meal list for that area if it is valid
    """
    if verify_area(area):
        meals = requests.get_meals_by_area(area)
        if meals is None:
            print("Technical difficulties, please try again later.")
        else:
            print_meals(title=area.upper(), meals=meals)
    else:
        print("Invalid area")


def main():
    """
    This is the main method
    """
    display_title()
    display_menu()

    while True:
        choice = None
        while choice is None:
            choice = get_menu_choice()
        display_menu_item_by_choice(choice)


if __name__ == "__main__":
    main()
