from typing import Dict
from Card import Card


class CreatureCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
        ) -> None:
        super().__init__(
            name,
            cost,
            rarity
        )
        if attack < 1 or health < 0:
            raise ValueError("atack and health must be positive and more than 0")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_player": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_result": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self):
        base_info = super().get_card_info()
        base_info.update({
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
            })
        return base_info
