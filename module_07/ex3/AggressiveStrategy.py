from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        card_players = []
        mana_used = 0
        damage_dealt = 0

        for card in list(hand):
            if card.name in ["Goblin Warrior", "Lightning Bolt"]:
                result = card.play({})
                card_players.append(card.name)
                mana_used += result.get("mana_used", 0)

                if hasattr(card, "attack_power"):
                    battlefield.append(card)
                if "damage" in str(result.get("effect", "")):
                    damage_dealt += 3

        for creature in battlefield:
            if hasattr(creature, "attack_power"):
                damage_dealt += creature.attack_power

        targets = self.prioritize_targets(["Enemy Player", "Enemy Creature"])

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "card_players": card_players,
                "mana_used": mana_used,
                "targets_attacked": [targets[0]],
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        priority_list = sorted(
            available_targets,
            key=lambda x: 0 if x == "Enemy Player" else 1
        )
        return priority_list
