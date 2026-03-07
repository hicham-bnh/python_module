from typing import List, Callable, Dict, Any
import functools
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    if operation == "add":
        result = functools.reduce(operator.add, spells)
        return result
    if operation == "multiply":
        result = functools.reduce(operator.mul, spells)
        return result
    if operation == "max":
        result = functools.reduce(lambda x, y: x if x > y else y, spells)
        return result
    if operation == "min":
        result = functools.reduce(lambda x, y: x if x < y else y, spells)
        return result
    else:
        result = 0
        return result


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, power=50, element="fire"
            ),
        "ice_enchant": functools.partial(
            base_enchantment, power=50, element="ice"
            ),
        "lightnin_enchant": functools.partial(
            base_enchantment, power=50, element="lightnin"
            )
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    a, b = 0, 1
    i = 0
    while (i < n):
        a, b = b, a + b
        i += 1
    return a


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def base_spell(spell) -> str:
        return f"unknown {spell}"

    @base_spell.register(int)
    def _(spell: int) -> str:
        return f"spell: {spell} points"

    @base_spell.register(str)
    def _(spell: str) -> str:
        return f"casting : {spell}"

    @base_spell.register(list)
    def _(spell: List) -> Any:
        spell_names = ", ".join(map(str, spell))
        return f"Multi-casting: {spell_names}"
    return base_spell


if __name__ == "__main__":
    num = [1, 8, 9, -2]
    print("\nTesting spell reducer...")
    sum = spell_reducer(num, "add")
    product = spell_reducer(num, "multiply")
    max = spell_reducer(num, "max")
    print(f"Sum: {sum}")
    print(f"Product: {product}")
    print(f"Max: {max}")
    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
