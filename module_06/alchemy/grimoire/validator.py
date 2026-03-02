def validate_ingredients(ingredients: str) -> str:
    all_ingredients = ["fire", "water", "earth", "air"]

    for i in ingredients.split():
        if i not in all_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
