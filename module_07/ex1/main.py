from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")
    light_bolt = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="commom",
        effect_type="damage",
    )
    mana_crystal = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=5,
        effect="+1 mana per tur"
    )
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    deck = Deck()
    deck.add_card(light_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    status = deck.get_deck_stats()
    print(f"Deck stats: {status}")
    print()
    print("Drawing and playing cards:")
    print()
    game_state = {"mana": 10, "active_creatures": [], "active_artifacts": []}

    for _ in range(3):
        card = deck.draw_card()
        if card:
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"Drew: {card.name} ({card_type})")

            result = card.play(game_state)
            print(f"Play result: {result}\n")
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
