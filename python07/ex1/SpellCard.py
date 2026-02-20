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
        return {
            "card_player": self.name,
            "mana_used": 3,
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: List) -> Dict:
        effect = {
            "card_played": self.name,
            "targets": [target.name for target in targets]
        }
        value = [int(s) for s in str.split(self.effect_type) if s.isdigit()]
        effect.update({"value": value})
        for target in targets:
            if "damage" in self.effect_type:
                target.health -= value
                effect.update({"effect": "damage"})
            elif "heal" in self.effect_type:
                target.health += value
                effect.update({"effect": "heal"})
        return effect
