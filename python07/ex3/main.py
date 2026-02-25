from ex3.FantasyCardFactory import FanstasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


if __name__ == "__main__":
    strategy = AggressiveStrategy()
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print(f"Strategy: {strategy.get_strategy_name()}")