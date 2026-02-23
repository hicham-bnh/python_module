from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List, Dict


class EliteCard(Card, Magical, Combatable):
    def play(self, gmae_state: Dict) -> Dict:
        return {

        }
    
    def attack(self, target) -> Dict:
        return {

        }
    
    def cast_spell(self, spll_name: str, target: List) -> Dict:
        return {
            
        }