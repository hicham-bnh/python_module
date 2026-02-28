from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamenPlatform


if __name__ == "__main__":
    card1: TournamentCard = TournamentCard("Fire Dragon", 1200, 0, 0, "dragon_001", 20, 50)
    card2: TournamentCard = TournamentCard("Ice Wizard", 1150, 0, 0, "wizard_001", 15, 20)
    tornament: TournamenPlatform = TournamenPlatform()
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    print(tornament.register_card(card1))
    print()
    print(tornament.register_card(card2))
    print("\nCreating tournament match...")
    match_result = tornament.create_match('dragon_001', 'wizard_001')
    print(f"Match result: {match_result}\n")
    print("Tournament Leaderboard:")
    result = tornament.get_leaderboard()
    i = 1
    for _ in range(len(result)):
        print(f"{i}. {result[_]}")
        i += 1
    print("\nPlatform Report:")
    print(tornament.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
