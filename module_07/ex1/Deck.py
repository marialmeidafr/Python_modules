import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self._cards)
        if total == 0:
            return {"total_cards": 0, "avg_cost": 0.0}

        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard
        from ex0.CreatureCard import CreatureCard

        for card in self._cards:
            total_cost += card.cost

            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1

        avg_cost = total_cost / total

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 1)
        }
