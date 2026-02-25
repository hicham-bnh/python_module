from ex3.CardFactory import CardFactory
from typing import Dict
from ex0.Card import Card


class FanstasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass
    
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass
    
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass
    
    def create_themed_deck(self, size: int) -> Dict:
        pass
    
    def get_supported_types(self) -> Dict:
        pass