import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []


    def add_card(self, card: Card) -> None:
        self.cards.append(card)


    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.card):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False
    

    def shuffle(self) -> None:
        random.shuffle(self.cards)


    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards.pop()
    

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        info = {
            "total_cards": total_cards,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }

        if total_cards == 0:
            return info

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost

            if isinstance(card, CreatureCard):
                info["creatures"] += 1
            elif isinstance(card, SpellCard):
                info["spells"] += 1
            elif isinstance(card, ArtifactCard):
                info["artifacts"] += 1
        info["avg_cost"] = round(float(total_cost / total_cards), 1)
        
        return info
