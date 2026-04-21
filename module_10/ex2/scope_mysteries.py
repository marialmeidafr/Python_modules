from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    """Create a counter function that increments an internal value."""
    count = 0

    def counter() -> int:
        """Increase and return the current counter value."""
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Create an accumulator that adds power to a running total."""
    total_power = initial_power

    def accumulator(power: int) -> int:
        """Add the given power and return the updated total."""
        nonlocal total_power
        total_power += power
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a formatter that prefixes items with an enchantment type."""
    def factory(item_name: str) -> str:
        """Build the enchanted item name."""
        return f"{enchantment_type} {item_name}"
    return factory


def memory_vault() -> dict[str, Callable]:
    """Create a simple key-value vault with store and recall operations."""
    storage = {}

    def store(key: str, value: Any) -> None:
        """Store a value under the given key."""
        storage[key] = value

    def recall(key: str) -> Any:
        """Return a stored value or a default message when missing."""
        return storage.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """Run a quick demonstration of closures and local scope behavior."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    add = spell_accumulator(100)
    print(f"Base 100, add 20: {add(20)}")
    print(f"Base 100, add 30: {add(30)}")
    print()
    print("Testing enchantment factory...")
    fire_enchanter = enchantment_factory("Flaming")
    print(fire_enchanter("Sword"))
    ice_enchanter = enchantment_factory("Frozen")
    print(ice_enchanter("Shield"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']("secret", 42)

    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
