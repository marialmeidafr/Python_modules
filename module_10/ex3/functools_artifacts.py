import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spells using the requested operation."""
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial enchantments for each elemental spell type."""
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Compute Fibonacci numbers with memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a dispatcher that formats spells by input type."""
    @functools.singledispatch  # única função execute códigos
    # diferentes dependendo do tipo do dado enviado como argumento
    def base_spell(arg: Any) -> str:
        """Handle spell values with no registered specialized type."""
        return "Unknown spell type"

    @base_spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @base_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @base_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return base_spell


def main() -> None:
    """Run a quick demonstration of the module functions."""
    print("Testing spell reducer...")
    numbers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(numbers, 'add')}")
    print(f"Product: {spell_reducer(numbers, 'multiply')}")
    print(f"Min: {spell_reducer(numbers, 'min')}")
    print(f"Max: {spell_reducer(numbers, 'max')}")

    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()
    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(2.1))


if __name__ == "__main__":
    main()
