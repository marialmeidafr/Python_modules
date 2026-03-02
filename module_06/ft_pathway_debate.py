import alchemy.transmutation as transmutation
import alchemy


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", transmutation.basic.lead_to_gold())
    print("stone_to_gem():", transmutation.basic.stone_to_gem())
    print()
    print("Testing Relative Imports (from advanced.py):")
    print("philosophers_stone():", transmutation.advanced.philosophers_stone())
    print("elixir_of_life():", transmutation.advanced.elixir_of_life())
    print()
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold() ->",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): [same as above]")
    print()
    print("Both pathways work! Absolute: clear, Relative: concise")
