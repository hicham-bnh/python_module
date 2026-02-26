from .GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: card["cost"])

        mana_limit = 5
        mana_used = 0
        damage = 0
        cards_played = []

        for card in sorted_hand:
            if mana_used + card["cost"] <= mana_limit:
                mana_used += card["cost"]
                damage += card.get("damage", 0)
                cards_played.append(card["name"])

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
