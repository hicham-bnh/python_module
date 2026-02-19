from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck

if __name__ == "__main__":
    deck = Deck()
    card_spel = SpellCard(
        "Lightning Bolt",
        4,
        "Spell",
        "Deal 3 damage to target"
    )
    card_creature = CreatureCard(
        "Fire Dragon",
        4,
        "Creature",
        4,
        4
    )
    card_artifact = ArtifactCard(
        "Mana Crystal",
        4,
        "Artifact",
        1,
        "Permanent: +1 mana per turn"
    )
    deck.add_card(card_spel)
    deck.add_card(card_creature)
    deck.add_card(card_artifact)
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    print(deck.get_deck_stats())
    print("Drawing and playing cards:\n")
