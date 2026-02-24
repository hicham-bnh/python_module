from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List, Dict


class EliteCard(Card, Magical, Combatable):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            damage: int,
            combat_type: str,
            health: int
        ) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.health = health

    def play(self, gmae_state: Dict) -> Dict:
        return {

        }
    
    def attack(self, target) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }
    
    def cast_spell(self, spll_name: str, target: List) -> Dict:
        return {
            
        }