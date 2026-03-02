from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:

    status = validate_ingredients(ingredients)
    if "VALID" in status:
        return f"Spell recorded: {spell_name} ({status})"
    return f"Spell rejected: {spell_name} ({status})"
