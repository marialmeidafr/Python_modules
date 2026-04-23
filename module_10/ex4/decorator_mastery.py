import functools
import time
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
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
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power: int, *args: Any, **kargs: Any) -> Any:
            if power >= min_power:
                return func(power, *args, **kargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def 


def main() -> None:
    print("Testing spell timer...")
    print(spell_timer("fireball"))
    print("Result: ")
    print()
    print("Testing retrying spell...")
    print("Waaaaaaagh spelled !")
    print()
    print("Testing MageGuild...")


if __name__ == "__main__":
    main()
