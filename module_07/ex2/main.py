from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    print("EliteCard capabilities:")
    
    cards_methods = ['play', 'get_card_info', 'is_playable']

    combat_methods = []
    for method in dir(Combatable):
        if not method.startswith('_'):
            combat_methods.append(method)

    magic_methods = []
    for method in dir(Magical):
        if not method.startswith('_'):
            magic_methods.append(method)
    
    print(f"- Card: {cards_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")
    print()
    warrior = EliteCard("Arcane Warrior", 5, "Legendary")
    print(f"Playing {warrior.name} (Elite Card):")
    print()
    print("Combat phase:")
    attack_res = warrior.attack("Enemy")
    print(f"Attack result: {attack_res}")
    defense_res = warrior.defend(5)
    print(f"Defense result: {defense_res}")
    print()
    print("Magic phase:")
    spell_res = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")
    mana_channel = warrior.channel_mana(3)
    print(f"Mana channel: {mana_channel}")
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
