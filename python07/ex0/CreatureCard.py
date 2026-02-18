from typing import Dict


class CreatureCard():
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            health: int
        ) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: Dict) -> Dict:
        pass

    def attack_target(self, target) -> Dict:
        pass