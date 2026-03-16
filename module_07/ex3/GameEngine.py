from typing import Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        deck_data = factory.create_themed_deck(3)
        self.hand = deck_data.get('card', [])
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError(
                "Engine not configured with factory or strategy"
            )

        self.turns_simulated += 1
        turn_result = self.strategy.execute_turn(self.hand, self.battlefield)

        actions = turn_result.get("actions", {})
        damage = actions.get("damage_dealt", 0)
        self.total_damage += damage

        return turn_result

    def get_engine_status(self) -> dict:
        strategy_name = (
            self.strategy.get_strategy_name() if self.strategy else None
        )
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
