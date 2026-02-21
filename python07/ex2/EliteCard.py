from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.damage = 0
        self.health = 0
        self.mana = 0

    def play(self, game_state: Dict) -> Dict:
        print(f"Playing {self.name} (Elite Card)")
        self.mana = game_state['mana']
        self.damage = game_state['attack']
        self.health = game_state['health']
        return {
            "name": self.name,
            "mana": self.attack,
            "attack": self.damage,
            "health": self.health
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": "melee"
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        self.mana -= 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targtes": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }

    def defend(self, incoming_damage: int) -> Dict:
        block: int = 3
        if block < incoming_damage:
            self.health -= (incoming_damage - block)
        else:
            incoming_damage = block
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - block,
            "damage_blocked": block,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.damage
        }
