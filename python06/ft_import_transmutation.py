import alchemy
from alchemy import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion

print("\n=== Import Transmutation Mastery ===\n")
print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.create_fire()}")
print()
print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}")
print()
print("Method 3 - Aliased import:")
print(f"heal(): {heal()}")
print()
print("Method 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")
print("\nAll import transmutation methods mastered!")
