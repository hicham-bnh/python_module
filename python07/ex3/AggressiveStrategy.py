from abc import ABC, abstractmethod
from typing import Dict, List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: List) -> Dict:
        return {

        }
    
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
    
    def prioritize_targets(self, available_targets: List) -> List:
        return [

        ]
