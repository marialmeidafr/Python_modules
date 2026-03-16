from ex0.CreatureCard import CreatureCard


def main() -> None:

    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    print("CreatureCard Info:")
    fire_dragon = CreatureCard(
        name="FireDragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
        )
    info_card = fire_dragon.get_card_info()
    print(info_card)
    print()
    print(f"Playing {fire_dragon.name} with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(7)}")
    game_state: dict = {"active_creatures": []}
    play_result = fire_dragon.play(game_state)
    print(f"Play result: {play_result}")
    print()
    print(f"{fire_dragon.name} attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {attack_result}")
    print()
    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(4)}")
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
