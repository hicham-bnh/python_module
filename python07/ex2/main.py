from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    elite_card = EliteCard("Arcane Warrior", 3, "Legend", 5, "melee", 8)
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()
    print("Playing Arcane Warrior (Elite Card)\n")
    print("Combat phase:")
    print(f"Attack result: {elite_card.attack('Enemy')}")
    print(f"Defense result: {elite_card.defend(5)}")