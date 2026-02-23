from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard


def get_type(card: Card) -> str:
    if isinstance(card, CreatureCard):
        return "creature"
    if isinstance(card, SpellCard):
        return "spell"
    if isinstance(card, ArtifactCard):
        return "artifact"
    return "error"


if __name__ == "__main__":
    deck = Deck()
    creature_card = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )
    spell_card = SpellCard(
        "Lightning Bolt",
        3,
        "Common",
        "damage"
    )
    artifact_card = ArtifactCard(
        "Mana Crystal",
        2,
        "Common",
        5,
        "Permanent: +1 mana per turn"
    )
    deck.add_card(creature_card)
    deck.add_card(spell_card)
    deck.add_card(artifact_card)
    deck.shuffle()
    game_state = {
        "effect_creature": ""
    }
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")
    card_drew = deck.draw_card()
    game_state = {
        "effect_creature": "Creature summoned to battlefield"
    }
    print(f"Drew: {card_drew.name} ({get_type(card_drew)})")
    print(f"Play result: {card_drew.play(game_state)}")
    print()
    card_drew = deck.draw_card()
    print(f"Drew: {card_drew.name} ({get_type(card_drew)})")
    print(f"Play result: {card_drew.play(game_state)}")
    print()
    card_drew = deck.draw_card()
    print(f"Drew: {card_drew.name} ({get_type(card_drew)})")
    print(f"Play result: {card_drew.play(game_state)}")
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")
