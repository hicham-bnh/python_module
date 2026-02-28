from .TournamentCard import TournamentCard
from typing import Dict, List


class TournamenPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.match: int = 0
        self.total_rating: int = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return (
            f"{card.name} (ID: {card.card_id}):\n"
            "- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.win}-{card.lose}"
            )

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]
        winner, loser = (c1, c2) if c1.damage >= c2.damage else (c2, c1)
        winner.update_wins(1)
        loser.update_losses(1)
        self.match += 1
        return {
            'winner': winner.card_id,
            'loser': loser.card_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> List:
        sorted_cards = sorted(
            self.cards.values(), key=lambda x: x.rating, reverse=True
        )
        return [
            f"{c.name} - Rating: {c.rating} ({c.win}-{c.lose})"
            for c in sorted_cards
            ]

    def generate_tournament_report(self) -> Dict:
        try:
            avg = self.total_rating / len(self.cards)
        except ZeroDivisionError as e:
            print(e)
        finally:
            return {
                "total_cards": len(self.cards),
                "matches_played": self.match,
                "avg_rating": int(avg),
                "platfrom_satus": 'active'
            }
