from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type


    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
           raise ValueError("game_state must be a dictionary")

        targets = game_state.get("targets", [])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect(targets),
        }


    def resolve_effect(self, targets: None) -> dict:
        if targets is None:
            targets = []
        if self.name == "Lightning Bolt":
            return "Deal 3 damage to target"
        print(f"{self.effect_type}")
