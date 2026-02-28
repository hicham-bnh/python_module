from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")
    engine: GameEngine = GameEngine()
    factory: FantasyCardFactory = FantasyCardFactory()
    strategy: AggressiveStrategy = AggressiveStrategy()
    engine.configure_engine(factory, strategy)
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()
    print("\nTurn execution:")
    print("Strategy:", result["strategy"])
    print("Actions:", engine.simulate_turn())
    print("\nGame Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern:", end=" ")
    print("Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
