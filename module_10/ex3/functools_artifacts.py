import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max, 
        "min": min
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    