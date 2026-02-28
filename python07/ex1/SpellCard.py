from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict) -> Dict:
        if self.effect_type == "damage":
            effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            effect = "Deal 3 heal to targe"
        elif self.effect_type == "buff":
            effect = "Deal 3 buff to targe"
        elif self.effect_type == "debuff":
            effect = "Deal 3 debuff to targe"
        self.resolve_effect([])
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "effect": f"spell throw on {targets}"
        }
