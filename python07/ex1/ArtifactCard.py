from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
        ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: Dict) -> Dict:
        pass

    def activate_ability(self) -> Dict:
        pass