from ex2.Combatable import Combatable
from ex0.Card import Card
from .Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Rankable, Combatable):
    def __init__(
            self,
            name: str,
            rating: int,
            win: int,
            lose: int,
            card_id: str,
            attack: int,
            health: int
    ) -> None:
        self.name = name
        self.rating = rating
        self.win = win
        self.lose = lose
        self.card_id = card_id
        self.damage = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "player1": game_state['player1']

        }

    def attack(self, target: 'TournamentCard') -> Dict:
        target.defend(self.damage)
        return {
                "attacker": self.card_id,
                "target": target.card_id,
                "damage": self.damage
                }

    def defend(self, incoming_damage: int) -> Dict:
        self.health -= incoming_damage
        return {
            "card_id": self.card_id,
            "remaining_health": self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> Dict:
        return {**self.get_rank_info(), "name": self.name}

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.damage,
            "healt": self.health
        }

    def update_losses(self, losses: int) -> None:
        self.lose += losses
        self.rating -= losses * 15

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "record": f"{self.win}-{self.lose}"
        }

    def update_wins(self, wins: int) -> None:
        self.win += wins
        self.rating += wins * 15
