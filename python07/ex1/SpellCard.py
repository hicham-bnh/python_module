from ex0.Card import Card
from typing import Dict, List


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: Dict) -> Dict:
        pass

    def resolve(self, targets: List) -> Dict:
        pass