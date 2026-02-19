from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self) -> Dict:
        return {
            "card_player": self.name,
            "mana_used": 3,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            ""
        }