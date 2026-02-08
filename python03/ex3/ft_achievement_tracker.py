"""
Achievement Tracker System

This program analyzes player achievements using set operations,
including unions, intersections, and differences, to identify
common, unique, and rare achievements among players.
"""
if __name__ == "__main__":
    alice = set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))
    bob = set(('first_kill', 'level_10', 'boss_slayer', 'collector'))
    charlie = set(('level_10', 'treasure_hunter', 'boss_slayer',
                   'speed_demon', 'perfectionist'))
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    print("All unique achievements ", alice.union(charlie, bob))
    print("Total unique achievements:", len(alice.union(charlie, bob)))
    print()
    print("Common to all players:", alice.intersection(bob, charlie))
    rare_alice = alice.difference(charlie).difference(bob)
    rare_bob = bob.difference(alice).difference(charlie)
    rare_charlie = charlie.difference(alice).difference(bob)
    rare = rare_alice.union(rare_bob, rare_charlie)
    print("Rare achievements (1 player):", rare)
    print()
    print("Alice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))
