from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, List


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            combat_type: str,
            damage: int,
            damage_bloque: int,
            health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.combat_type = combat_type
        self.damage = damage
        self.damage_bloque = damage_bloque
        self.health = health
        self.damage_total: int = 0
        self.bloque_total: int = 0
        self.total_spell: int = 0
        self.total_mana_channel: int = 0

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        self.cost -= 4
        self.total_spell += 1
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> Dict:
        self.cost += amount
        self.total_mana_channel += amount
        return {
            "channeled": amount,
            "total_mana": self.cost
        }

    def get_magic_stats(self) -> Dict:
        return {
            "all_spell_played": self.total_spell,
            "all_mana_channeled": self.total_mana_channel
        }

    def attack(self, target) -> Dict:
        self.damage_total += self.damage
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict:
        if incoming_damage < self.damage_bloque:
            damage_blq = incoming_damage
        else:
            damage_blq = self.damage_bloque
        damage_taken = incoming_damage - self.damage_bloque
        if damage_taken < 0:
            damage_taken = 0
        self.health -= damage_taken
        self.bloque_total += damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_bloqued": damage_blq,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "total_damage": self.damage_total,
            "total_damage_bloque": self.bloque_total
        }

    def play(self, game_state: Dict) -> Dict:
        game_state = {
            "player": self.name,
            "attack": self.damage,
            "health": self.health,
            "mana": self.cost
        }
        return game_state
