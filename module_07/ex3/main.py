from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    engine.configure_engine(factory, strategy)
    print(f"Available types: {factory.get_supported_types()}")
    print()
    print("Simulating aggressive turn...")
    hand_display = [f"{c.name} ({c.cost})" for c in engine.hand]
    print(f"Hand: {hand_display}")
    print()
    print("Turn execution:")
    try:
        turn = engine.simulate_turn()
        print(f"Strategy: {turn['strategy']}")
        print(f"Actions: {turn['actions']}")
    except RuntimeError as e:
        print(f"Error: {e}")
    print()
    print("Game Report:")
    print(engine.get_engine_status())
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
