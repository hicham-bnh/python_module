from ex0.Card import Card
from typing import Dict, List
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
import random


class Deck:
    def __init__(self) -> None:
        self.deck_card: List = []
        self.card_total: int = 0
        self.card_creature: int = 0
        self.card_spell: int = 0
        self.card_artifact: int = 0
        self.cost_total: int = 0

    def add_card(self, card: Card) -> None:
        if isinstance(card, SpellCard):
            self.card_spell += 1
            self.cost_total += card.cost
        elif isinstance(card, CreatureCard):
            self.card_creature += 1
            self.cost_total += card.cost
        elif isinstance(card, ArtifactCard):
            self.card_artifact += 1
            self.cost_total += card.cost
        self.deck_card.append(card)
        self.card_total += 1

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck_card:
            if card.name == card_name:
                self.deck_card.remove(card)
                if isinstance(card, SpellCard):
                    self.card_spell -= 1
                elif isinstance(card, CreatureCard):
                    self.card_creature -= 1
                elif isinstance(card, ArtifactCard):
                    self.card_artifact -= 1
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck_card, random.random)

    def draw_card(self) -> Card:
        return self.deck_card.pop(0)

    def get_deck_stats(self) -> Dict:
        try:
            avg: float = self.cost_total / self.card_total
        except ZeroDivisionError as e:
            print(f"ERROR: {e}")
        return {
            "total_cards": self.card_total,
            "creatures": self.card_creature,
            "spells": self.card_spell,
            "artifacts": self.card_artifact,
            "avg_cost": round(avg, 1)
        }
