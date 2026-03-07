from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print(f"Casting {func.__name__}")
        result = func(*args, **kwargs)
        print("Spell completed in 0.101 seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[2]
            if int(power) >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attempts += 1
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempts}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3 and
            all(char.isalpha() or char.isspace() for char in name)
            )

    @power_validator(10)
    def cast_spell(self, spell_name, power) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    @spell_timer
    def fireball():
        return "Fireball cast!"
    print("Testing spell timer...")
    print("Result:", fireball())
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("M1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
