from ex2.EliteCard import EliteCard


if __name__ == "__main__":
    elite_card = EliteCard("Arcane Warrior",)
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
    game_stat = {
        "mana": 10,
        "attack": 5,
        "health": 10
    }
    elite_card.play(game_stat)
    print("\nCombat phase:")
    print(f"Attack result: {elite_card.attack('Enemy')}")
    print(f"Defense result: {elite_card.defend(5)}")
    print()
    print("Magic phase:")
    print("Spell cast: ", end=" ")
    print(f"{elite_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite_card.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")
