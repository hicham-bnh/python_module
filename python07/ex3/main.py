from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine.configure_engine(factory, strategy)
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    print("\nTurn execution:")
    print("Strategy:", result["strategy"])
    actions = result.copy()
    del actions["strategy"]
    print("Actions:", actions)
    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()