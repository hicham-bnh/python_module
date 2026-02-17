from typing import List


def validate_ingredients(ingredients: str) -> str:
    list_ingredient: List[str] = [x for x in ingredients.split()]
    valid_ingredients = ("fire", "water", "earth", "air")
    for x in range(len(list_ingredient)):
        if list_ingredient[x] in valid_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
