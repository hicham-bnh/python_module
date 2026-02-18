from CreatureCard import CreatureCard

if __name__ == "__main__":

    card = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(card.get_card_info())
    print()
    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", card.is_playable(6))
    print("Play result", card.play({}))
    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", card.attack_target("Goblin Warrior"))
    print("\nTesting insufficient mana (3 available):")
    print("Playable:", card.is_playable(3))
    print("\nAbstract pattern successfully demonstrated!")
