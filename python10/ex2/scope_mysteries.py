from typing import Callable, Dict


def mage_counter() -> Callable:
    call = 0

    def call_check() -> int:
        nonlocal call
        call += 1
        return call
    return call_check


def apell_accumulator(initial_power: int) -> Callable:
    apl = initial_power

    def apell(amount: int) -> int:
        nonlocal apl
        apl += amount
        return apl
    return apell


def enchantment_factory(enchantment_type: str) -> Callable:

    def result(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return result


def memory_vault() -> Dict[str, Callable]:
    memory = {}

    def store(key, value) -> None:
        memory[key] = value

    def recall(key) -> Dict:
        return memory.get(key, "Memory not found")
    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    count = mage_counter()
    test1 = enchantment_factory("Flaming")
    test2 = enchantment_factory("Frozen")
    print("\nTesting mage counter...")
    print(f"Call 1: {count()}")
    print(f"Call 2: {count()}")
    print(f"Call 3: {count()}")
    print("\nTesting enchantment factory...")
    print(test1('Sword'))
    print(test2('Shield'))
