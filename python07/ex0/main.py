from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    gane_state = {
        "effect_creature": "Creature summoned to battlefield"
    }
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(creature_card.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(6)}")
    print(f"Play result: {creature_card.play(gane_state)}")
    print(f"Attack result: {creature_card.attack_target('Goblin Warrior')}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")
