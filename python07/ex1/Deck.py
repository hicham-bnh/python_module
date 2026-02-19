from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from typing import Dict, List
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random

class Deck():
    def __init__(self) -> None:
        self.decks: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.decks.append(card)

    def remove_card(self, card_name: Card) -> bool:
        for card in self.decks:
            if card.name == card_name:
                self.decks.remove(card_name)
                return True
        return False


    def shuffle(self) -> None:
        random.shuffle(self.decks)

    def draw_card(self) -> Card:
        print(f"Drew: {self.decks[0].name} ({self.decks[0].rarity})")
        self.remove_card(self.decks[0])
        return self.decks[0]

    def get_deck_stats(self) -> Dict:
        total_card: int = len(self.decks)
        creature: int = 0
        spells: int = 0
        artifacts: int = 0
        cost: int = 0
        avg_cost: float = 0.0
        for card in self.decks:
            if isinstance(card, CreatureCard):
                cost += card.cost
                creature += 1
            if isinstance(card, SpellCard):
                cost += card.cost
                spells += 1
            if isinstance(card, ArtifactCard):
                cost += card.cost
                artifacts += 1
        avg_cost = cost / total_card
        return {
        'total_cards': total_card,
        'creatures': creature,
        'spells': spells,
        'artifacts': artifacts,
        'avg_cost': avg_cost
        }

        
            
