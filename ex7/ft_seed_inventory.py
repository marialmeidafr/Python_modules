def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    first_word = seed_type.capitalize()

    if unit == "packets":
        print(first_word, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(first_word, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(first_word, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
