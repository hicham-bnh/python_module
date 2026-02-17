import alchemy.grimoire
from alchemy.grimoire.spellbook import record_spell

print("\n=== Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
print("validate_ingredients(\"fire air\"):",
      alchemy.grimoire.validate_ingredients("fire air"))
print("validate_ingredients(\"dragon scales\"):",
      alchemy.grimoire.validate_ingredients("dragon scales"))
print("\nTesting spell recording with validation:")
print("record_spell(\"Fireball\", \"fire air\"):",
      alchemy.grimoire.record_spell("Fireball", "fire air"))
print("record_spell(\"Dark Magic\", \"shadow\"):",
      alchemy.grimoire.record_spell("Dark Magic", "shadow"))
print("\nTesting late import technique:")
print("record_spell(\"Lightning\", \"air\"):",
      record_spell("Lightning", "air"))
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
