from alchemy.grimoire import validate_ingredients, record_spell


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    val_1 = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {val_1}')
    val_2 = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {val_2}')
    print()
    print("Testing spell recording with validation:")
    val_3 = record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {val_3}')
    val_4 = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {val_4}')
    print()
    print("Testing late import technique:")
    val_5 = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {val_5}')
    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")
