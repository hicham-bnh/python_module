from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": game_state.get('effect_creature')
        }

    def attack_target(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__,
            "attack": self.attack,
            "health": self.health
        }
