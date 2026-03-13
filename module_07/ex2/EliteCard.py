from typing import Any, Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Combatable, Magical, Card):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = 5
        self.health = 10
        self.mana_pool = 7
        self.effect = "Elite card enters the battlefield"


    def play(self, game_state) -> Dict[str, Any]:
        return {
            **game_state,
            'card_played' : self.name,
            'mana_used' : self.cost,
            'effect' : self.effect
        }
    

    def attack(self, target) -> Dict[str, Any]:
        return {
            'attacker' : self.name,
            'target' : target,
            'damage' : self.attack_power,
            'combat_type' : "melee"
        }


    def defend(self, incoming_damage) -> Dict[str, Any]:
        taken = int(incoming_damage * 0.4)
        blocked = incoming_damage - taken
        self.health -= taken
        return {
            'defender' : self.name,
            'damage_taken' : taken,
            'damage_blocked' : blocked,
            'still_alive' : True
        }


    def get_combat_stats(self) -> Dict[str, Any]:
        return{'attack' : self.attack_power, 'health' : self.health}


    def cast_spell(self, spell_name: str, targets: List[Any]) -> Dict[str, Any]:
        return {
            'caster' : self.name,
            'spell' : spell_name,
            'targets' : targets,
            'mana_used' : self.cost
        }


    def channel_mana(self, amount: int) -> Dict[str, Any]:
        return {
            'channeled' : amount,
            'total_mana' : self.mana_pool
        }


    def get_magic_stats(self):
        return {'mana' : self.mana_pool}
