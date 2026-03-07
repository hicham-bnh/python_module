from typing import Callable, List, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args, **kwargs) -> Any:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> Callable:
        return (base_spell(*args, **kwargs) * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def check(*args, **kwargs) -> Any:
        if condition(*args, **kwargs):
            return True
        return "Spell fizzled"
    return check


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> List:
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


def fireball(taget: str) -> str:
    return f"Fireball hits {taget}"


def heal(target: str) -> str:
    return f"Heals {target}"


def power() -> int:
    return 10


def condition() -> bool:
    return True


if __name__ == "__main__":
    combined = spell_combiner(fireball, heal)
    mul = power_amplifier(power, 5)
    print("\nTesting spell combiner..")
    print("Combined spell result:", end=" ")
    print(f"{combined('Dragon')[0]}", end=",")
    print(f" {combined('Dragon')[1]}")
    print()
    print(f"Original: {power()}", end=" ")
    print(f"Amplified: {mul()}")
