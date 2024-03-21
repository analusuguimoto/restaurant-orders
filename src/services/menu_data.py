import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_menu(source_path)

    def load_menu(self, source_path):
        dishes = {}

        with open(source_path, "r") as doc:
            menu = csv.DictReader(doc)

            for info in menu:
                recipe = info["dish"]
                price = float(info["price"])
                ingredients = info["ingredient"]
                ingredient_amount = int(info["recipe_amount"])

                if recipe not in dishes:
                    dishes[recipe] = Dish(recipe, price)

                dishes[recipe].add_ingredient_dependency(
                    Ingredient(ingredients), ingredient_amount
                )

        return set(dishes.values())
