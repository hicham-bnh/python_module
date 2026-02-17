from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    lead_to_gold_result = lead_to_gold()
    healing_potion_result = healing_potion()
    return (
        f"Philosopher’s stone created using "
        f"{lead_to_gold_result} and "
        f"{healing_potion_result}"
        )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
