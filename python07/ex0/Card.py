from abc import ABC, abstractmethod
from typing import Dict

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    def play(self, gane_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        pass

    def is_playable(self, available_mana: int) -> bool:
        pass