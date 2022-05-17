from urllib import request
import json

from objects import Category, Meal

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


if __name__ == "__main__":
    get_categories()
