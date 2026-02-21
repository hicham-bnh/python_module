from typing import Dict
from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def attack(self, target) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
