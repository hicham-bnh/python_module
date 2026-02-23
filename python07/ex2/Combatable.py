from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> Dict:
        pass

    def defend(self, incoming_damage: int) -> Dict:
        return {

        }

    def get_combat_stats(self) -> Dict:
        return {
            
        }