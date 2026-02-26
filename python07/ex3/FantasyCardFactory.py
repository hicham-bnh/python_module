from .CardFactory import CardFactory

class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        return {"name": "Fire Dragon", "cost": 5, "damage": 5}

    def create_spell(self, name_or_power=None):
        return {"name": "Lightning Bolt", "cost": 3, "damage": 3}

    def create_artifact(self, name_or_power=None):
        return {"name": "Mana Ring", "cost": 1, "damage": 0}

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