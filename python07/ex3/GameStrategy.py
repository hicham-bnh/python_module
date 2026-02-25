from abc import ABC, abstractmethod
from typing import Dict, List


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        pass
