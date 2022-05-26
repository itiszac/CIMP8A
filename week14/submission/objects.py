class Category:
    """
    This class will represent a Category object.

    Attributes:
        __category (str): The name of the category.
    """

    def __init__(self, category):
        """
        This method will initialize a Category object.

        Args:
            category (str): The name of the category.
        """
        self.__category = category

    def get_name(self):
        """
        This method will return the name of the category.
        """
        return self.__category

    def set_name(self, category):
        """
        This method will assign the private attribute __category to the value provided.
        """
        self.__category = category


class Meal:
    """
    This class will represent a Meal object.

    Attributes:
        __meal_id (str): The id of the meal.
        __meal_name (str): The name of the meal.
        __meal_thumb (str): The thumbnail of the meal.
    """

    def __init__(self, meal_id, meal_name, meal_thumb):
        """
        This method will initialize a Meal object.

        Args:
            meal_id (str): The id of the meal.
            meal_name (str): The name of the meal.
            meal_thumb (str): The thumbnail of the meal.
        """
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        """
        This method will return the id of the meal.
        """
        return self.__meal_id

    def set_meal_id(self, meal_id):
        """
        This method will assign the private attribute __meal_id to the value provided.
        """
        self.__meal_id = meal_id

    def get_meal_name(self):
        """
        This method will return the name of the meal.
        """
        return self.__meal_name

    def set_meal_name(self, meal_name):
        """
        This method will assign the private attribute __meal_name to the value provided.
        """
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        """
        This method will return the thumbnail of the meal.
        """
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        """
        This method will assign the private attribute __meal_thumb to the value provided.
        """
        self.__meal_thumb = meal_thumb


class Recipe(Meal):
    """
    This class will represent a Recipe object.

    Attributes:
        __meal_ingredients (list): The list of ingredients for a meal.
        __meal_instructions (list): The list of instructions for a meal.
    """

    def __init__(self, meal_id, meal_name, meal_thumb):
        """
        This method will initialize a Recipe object.

        Args:
            meal_id (str): The id of the meal.
            meal_name (str): The name of the meal.
            meal_thumb (str): The thumbnail of the meal.
        """
        super().__init__(meal_id, meal_name, meal_thumb)
        self.__meal_ingredients = []
        self.__meal_instructions = []

    def get_meal_ingredients(self):
        """
        This method will return the ingredients of the meal.
        """
        return self.__meal_ingredients

    def set_meal_ingredients(self, meal_ingredients):
        """
        This method will assign the private attribute __meal_ingredients to the value provided.
        """
        self.__meal_ingredients = meal_ingredients

    def get_meal_instructions(self):
        """
        This method will return the instructions of the meal.
        """
        return self.__meal_instructions

    def set_meal_instructions(self, meal_instructions):
        """
        This method will assign the private attribute __meal_instructions to the value provided.
        """
        self.__meal_instructions = meal_instructions


class Areas:
    """
    This class will represent a Areas object.

    Attributes:
        __areas (list): The list of areas.
    """

    def __init__(self, areas):
        """
        This method will initialize a Areas object.

        Args:
            areas (list): The list of areas.
        """
        self.__areas = areas

    def get_areas(self):
        """
        This method will return the list of areas.
        """
        return self.__areas

    def set_areas(self, areas):
        """
        This method will assign the private attribute __areas to the value provided.
        """
        self.__areas = areas
