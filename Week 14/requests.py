from urllib import request
import json

from objects import Category, Meal, Recipe


def fix_url(url):
    """
    This function fixes urls including spaces and replaces with %20
    to be used in the request.
    """
    if " " in url:
        url = url.replace(" ", "%20")
    return url


def build_recipe_from_data(data):
    """
    This method will build a recipe from the data dictionary provided
    and return it as a Recipe object or None if the data is invalid.
    """
    recipe = None
    if len(data["meals"]) > 0:
        recipe = Recipe(
            data["meals"][0]["idMeal"],
            data["meals"][0]["strMeal"],
            data["meals"][0]["strMealThumb"],
        )
        recipe.set_meal_instructions(data["meals"][0]["strInstructions"])
        ingredients = []
        for i in range(1, 20):
            if (
                data["meals"][0]["strIngredient{}".format(i)] is not None
                and data["meals"][0]["strIngredient{}".format(i)] != ""
                and data["meals"][0]["strIngredient{}".format(i)] != " "
                and data["meals"][0]["strMeasure{}".format(i)] is not None
                and data["meals"][0]["strMeasure{}".format(i)] != ""
                and data["meals"][0]["strMeasure{}".format(i)] != " "
            ):
                ingredient = {}
                ingredient["measure"] = data["meals"][0]["strMeasure{}".format(i)]
                ingredient["ingredient"] = data["meals"][0]["strIngredient{}".format(i)]
                ingredients.append(ingredient)
        recipe.set_meal_ingredients(ingredients)
    return recipe


def build_meals_list_by_data(data):
    """
    This method will build a list of meals from the data dictionary provided
    and return it as a list of Meal objects or None if the data is invalid.
    """
    meals = []
    for meal in data["meals"]:
        meals.append(Meal(meal["idMeal"], meal["strMeal"], meal["strMealThumb"]))
    return meals


def get_categories():
    """
    This method will return a list of categories as Category objects.
    """
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    response = request.urlopen(url)
    categories = []
    try:
        data = json.loads(response.read().decode("utf-8"))
        for category in data["meals"]:
            categories.append(Category(category["strCategory"]))
    except (ValueError, KeyError, TypeError):
        categories = None
    return categories


def get_meals_by_category(category):
    """
    This method will return a list of meals as Meal objects from the category provided.
    """
    url = fix_url(
        "https://www.themealdb.com/api/json/v1/1/filter.php?c={}".format(category)
    )
    response = request.urlopen(url)
    try:
        data = json.loads(response.read().decode("utf-8"))
        meals = build_meals_list_by_data(data)
    except (ValueError, KeyError, TypeError):
        meals = None
    return meals


def get_recipe_by_name(name):
    """
    This method will return a recipe as a Recipe object from the name provided.
    """
    url = fix_url(
        "https://www.themealdb.com/api/json/v1/1/search.php?s={}".format(name)
    )
    response = request.urlopen(url)
    try:
        data = json.loads(response.read().decode("utf-8"))
        recipe = build_recipe_from_data(data)
    except (ValueError, KeyError, TypeError):
        recipe = None
    return recipe


def get_random_recipe():
    """
    This method will return a random recipe as a Recipe object.
    """
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    response = request.urlopen(url)
    try:
        data = json.loads(response.read().decode("utf-8"))
        recipe = build_recipe_from_data(data)
    except (ValueError, KeyError, TypeError):
        recipe = None
    return recipe


def get_areas():
    """
    This method will return a list of areas as an Area object.
    """
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    response = request.urlopen(url)
    areas = []
    try:
        data = json.loads(response.read().decode("utf-8"))
        for area in data["meals"]:
            areas.append(Category(area["strArea"]))
    except (ValueError, KeyError, TypeError):
        areas = None
    return areas


def get_meals_by_area(area):
    """
    This method will return a list of meals as Meal objects from the area provided.
    """
    url = fix_url(
        "https://www.themealdb.com/api/json/v1/1/filter.php?a={}".format(area)
    )
    response = request.urlopen(url)
    meals = []
    try:
        data = json.loads(response.read().decode("utf-8"))
        meals = build_meals_list_by_data(data)
    except (ValueError, KeyError, TypeError):
        meals = None
    return meals


if __name__ == "__main__":
    get_categories()
