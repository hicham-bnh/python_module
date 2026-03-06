from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power=None):
        card = CreatureCard("Fire Dragon", 5, "commun", 5, 8)
        return card

    def create_spell(self, name_or_power=None):
        card = SpellCard("Lightning Bolt", 3, "commun", "damage")
        return card

    def create_artifact(self, name_or_power=None):
        card = ArtifactCard("Mana Ring", 1, "commun", 5, "damage")
        return card

    def create_themed_deck(self, size: int) -> dict:
        deck = [
            {"name": "Fire Dragon", "cost": 5, "damage": 5},
            {"name": "Goblin Warrior", "cost": 2, "damage": 2},
            {"name": "Lightning Bolt", "cost": 3, "damage": 3}
        ]
        return {"deck": deck[:size]}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
