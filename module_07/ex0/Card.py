from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity


    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass


    def get_card_info(self) -> dict:
        """retorna dados da carta"""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """retorna um bool comparando o custo
        com a mana"""
        return available_mana >= self.cost
