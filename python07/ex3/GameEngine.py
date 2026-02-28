from .GameStrategy import GameStrategy
from .FantasyCardFactory import FantasyCardFactory


class GameEngine:
    def __init__(self):
        self.factory: FantasyCardFactory 
        self.strategy: GameStrategy
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: FantasyCardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {"error": "Engine not configured"}
        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data["deck"]
        formatted_hand = [f"{c['name']} ({c['cost']})" for c in hand]
        print("Hand: [" + ", ".join(formatted_hand) + "]")
        result = self.strategy.execute_turn(hand, ['enemy1'])
        self.turns_simulated += 1
        self.total_damage += result["damage_dealt"]
        self.cards_created += len(hand)
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
