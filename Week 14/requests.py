from urllib import request
import json

from objects import Category, Meal, Recipe

# Get a list of the meal categories
def get_categories():
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    response = request.urlopen(url)
    categories = []

    try:
        data = json.loads(response.read().decode("utf-8"))
        for category in data["meals"]:
            categories.append(Category(category["strCategory"]))

    except (ValueError, KeyError, TypeError):
        return None

    return categories


def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c={}".format(category)
    response = request.urlopen(url)
    meals = []

    try:
        data = json.loads(response.read().decode("utf-8"))
        for meal in data["meals"]:
            meals.append(Meal(meal["idMeal"], meal["strMeal"], meal["strMealThumb"]))

    except (ValueError, KeyError, TypeError):
        return None

    return meals


def get_recipe_by_name(name):
    if " " in name:
        name = name.replace(" ", "%20")
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s={}".format(name)
    response = request.urlopen(url)
    recipe = None

    try:
        data = json.loads(response.read().decode("utf-8"))
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
                    ingredient["ingredient"] = data["meals"][0][
                        "strIngredient{}".format(i)
                    ]
                    ingredients.append(ingredient)
            recipe.set_meal_ingredients(ingredients)

    except (ValueError, KeyError, TypeError):
        return None

    return recipe


if __name__ == "__main__":
    get_categories()
