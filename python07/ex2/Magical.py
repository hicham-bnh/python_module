from typing import Dict
from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
