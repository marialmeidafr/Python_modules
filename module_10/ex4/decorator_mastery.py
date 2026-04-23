import functools
import time
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Measure and print how long a spell function takes to run."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Allow a spell to run only when its power meets the minimum."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, power: int, *args: Any, **kargs: Any) -> Any:
            if power >= min_power:
                return func(self, power, *args, **kargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Retry a spell function until it succeeds or
    the attempts are exhausted.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
        return wrapper
    return decorator


class MageGuild:
    """Example guild that validates mage names and casts spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True when a mage name has at least three
        alphabetic characters.
        """

        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Cast a named spell when the requested power is high enough.
        """

        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Run a small demonstration of the decorators in this module."""

    print("Testing spell timer...")

    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"

    change_fireball = spell_timer(fireball)
    result = change_fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")

    def chaotic_ritual():
        raise ValueError("Chaos magic instability!")

    retry_logic = retry_spell(max_attempts=3)(chaotic_ritual)
    final_status = retry_logic()
    print(final_status)
    print("Waaaaaaagh spelled !")
    print()
    print("Testing MageGuild...")
    name1 = "testing"
    name2 = "with1"
    print(f"{MageGuild.validate_mage_name(name1)}")
    print(f"{MageGuild.validate_mage_name(name2)}")
    guild = MageGuild()
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5, "Spark"))


if __name__ == "__main__":
    main()
