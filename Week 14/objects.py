class Category:
    def __init__(self, category):
        self.__category = category

    def get_name(self):
        return self.__category

    def set_name(self, category):
        self.__category = category


class Meal:
    def __init__(self, meal_id, meal_name, meal_thumb):
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal_name(self):
        return self.__meal_name

    def set_meal_name(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Recipe(Meal):
    def __init__(self, meal_id, meal_name, meal_thumb):
        super().__init__(meal_id, meal_name, meal_thumb)
        self.__meal_ingredients = []
        self.__meal_instructions = []

    def get_meal_ingredients(self):
        return self.__meal_ingredients

    def set_meal_ingredients(self, meal_ingredients):
        self.__meal_ingredients = meal_ingredients

    def get_meal_instructions(self):
        return self.__meal_instructions

    def set_meal_instructions(self, meal_instructions):
        self.__meal_instructions = meal_instructions
