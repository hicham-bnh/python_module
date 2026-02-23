from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spll_name: str, target: List) -> Dict:
        pass

    def channel_mana(self, amout: int) -> Dict:
        return {
            
        }

    def get_magic_stats(self) -> Dict:
        return {
            
        }