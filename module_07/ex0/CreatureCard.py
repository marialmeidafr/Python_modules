from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
    
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a non-negative")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a non-negative")

        self.attack = attack
        self.health = health


    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionary")

        if "active_creatures" not in game_state:
            game_state["active_creatures"] = []

        game_state["active_creatures"].append(self.name)

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }


    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }


    def get_card_info(self):
        info = super().get_card_info()
        
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
