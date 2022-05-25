#! /usr/bin/env python3
import requests


def show_title():
    """
    This method will display the title screen
    """
    print("My Recipe Program")
    print()


def show_menu():
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
            return get_menu_choice()
    except ValueError:
        print("Invalid choice. Please enter a valid integer.")
        return get_menu_choice()
    return choice


def get_categories():
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


def get_meals():
    """
    This method will display the meals
    """
    category = input("Enter a category: ")
    meals = get_meals_by_category(category)
    if len(meals) > 0 and meals is not None:
        print(category.upper(), "MEALS")
        for m in meals:
            print("  " + m.get_meal_name())
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


def get_meals_by_category(category):
    """
    This method will prompt the user for a category
    and get the meal list for that category if it is valid
    """
    meals = []
    if verify_category(category):
        meals = requests.get_meals_by_category(category)
        if meals is None:
            print("Technical difficulties, please try again later.")
    else:
        print("Invalid category")
    return meals

def print_recipe(recipe):
    print("Recipe: " + recipe.get_meal_name())
    print()
    print("Instructions:\n" + recipe.get_meal_instructions())
    print()
    print("Ingredients:")
    print("Measure\t\tIngredient")
    for i in recipe.get_meal_ingredients():
        print(i)
    print()

def get_meal_by_name():
    """
    This method will prompt the user for a meal name
    and get the meal if it is valid
    """
    meal_name = input("Enter a meal name: ")
    print()
    meal = requests.get_recipe_by_name(meal_name)
    if meal is None:
        print("Technical difficulties, please try again later.")
    else:
        print_recipe(meal)

    return meal

def main():
    """
    This is the main method
    """
    show_title()
    show_menu()

    while True:
        choice = get_menu_choice()
        if choice == 1:
            get_categories()
        elif choice == 2:
            get_meals()
        elif choice == 3:
            get_meal_by_name()


if __name__ == "__main__":
    main()
