from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target) -> Dict:
        pass

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = incoming_damage - 3
        if damage_taken < 0:
            damage_taken = 0
        self.health -= damage_taken
        self.name = self.name
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": damage_taken,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            
        }