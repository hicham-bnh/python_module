from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    card: EliteCard = EliteCard(
        "Arcane Warrior",
        8,
        "Epique",
        "melee",
        5,
        3,
        10
        )
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(5)}")
    print()
    print("Magic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")
