from ex3.CardFactory import CardFactory
from typing import Dict, List, Any
from ex0.Card import Card
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
import random


class FanstasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_templates: list[tuple[Any, ...]] = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 5, 3),
        ]
        self.spell_templates: list[tuple[Any, ...]] = [
            ("Lightning Bolt", 3, "Rare", "Deal 3 damage to target"),
        ]
        self.artifact_templates: list[tuple[Any, ...]] = [
            ("Mana Ring", 2, "Rare", 3, "Permanent: +1 mana per turn"),
        ]
    creature: List[str] = []
    spell: List[str] = []
    artifact: List[str] = []

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power == "Goblin Warrior":
            name, cost, rarity, attack, healt = self.creature_templates[1]
            card = CreatureCard(name, cost, rarity, attack, healt)
            return (card)
        else:
            name, cost, rarity, attack, healt = self.creature_templates[0]
            card = CreatureCard(name, cost, rarity, attack, healt)
            return (card)

        
    
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        nm , cost, rarity, effect = self.spell_templates[0]
        card = SpellCard(nm, cost, rarity, effect)
        return card
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        nm, cost, rarity, dr, effect = self.artifact_templates[0]
        card = ArtifactCard(nm, cost, rarity, dr, effect)
        return card
    
    def create_themed_deck(self, size: int) -> Dict:
        deck = Deck()
        card1 = self.create_creature("Goblin Warrior")
        card2 = self.create_creature("")
        card3 = self.create_spell()
        card4 = self.create_artifact()
        deck.add_card(card1)
        deck.add_card(card2)
        deck.add_card(card3)
        deck.add_card(card4)
        return {
            "card 1": card1.name,
            "card 2": card2.name,
            "card 3": card3.name,
            "card 4": card4.name
        }
        
        
    
    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }