from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a spell that casts two spells with the same inputs."""

    def combination(target: str, power: int) -> tuple[str, str]:
        """Execute both spells and return their results as a tuple."""
        return (spell1(target, power), spell2(target, power))
    return combination


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a spell wrapper that multiplies incoming power."""

    def multiplication(target: str, power: int) -> str:
        """Cast the base spell with amplified power."""
        return base_spell(target, power * multiplier)
    return multiplication


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition is satisfied."""

    def conditional(target: str, power: int) -> str:
        """Evaluate condition and cast spell or return a fail message."""
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a caster that applies all spells in order."""

    def sequence(target: str, power: int) -> list[str]:
        """Cast every spell in the sequence using same target and power."""
        return [s(target, power) for s in spells]
    return sequence


def spell(target: str, power: int) -> str:
    """Deal fire damage to a target."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Restore hit points to a target."""
    return f"Heal restores {target} for {power} HP"


def main() -> None:
    """Run a small demo of higher-order spell helpers."""
    test_values = [3, 10, 18]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    print("Testing spell combiner...")
    combiner = spell_combiner(spell, heal)
    print(
        f"Combined spell result: {combiner(test_targets[0], test_values[0])}"
    )
    print()
    print("Testing power amplifier...")
    multiplier = 3
    amplifier = power_amplifier(spell, multiplier)
    print(
        f"Original: {test_values[1]}, "
        f"Amplified: {amplifier(test_targets[1], test_values[1])}"
    )
    print()
    print("Testing conditional caster...")

    def power_limit(target: str, power: int) -> bool:
        return power > 10

    conditional = conditional_caster(power_limit, spell)
    print(
        f"Target {test_targets[2]} with power {test_values[1]}: "
        f"{conditional(test_targets[2], test_values[1])}"
    )
    print(
        f"Target {test_targets[2]} with power {test_values[2]}: "
        f"{conditional(test_targets[2], test_values[2])}"
    )
    print()
    print("Testing spell sequence...")
    grimoire = [spell, heal, spell]
    sequence = spell_sequence(grimoire)
    print(f"Sequence results: {sequence(test_targets[3], test_values[0])}")


if __name__ == "__main__":
    main()
