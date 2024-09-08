from dataclasses import dataclass
from CardLib import CardSuperClass
from typing import List

@dataclass
class Deck:
    cards: List[CardSuperClass]
    name: str
    description: str

    def shuffle(self):
        # Add code to shuffle the deck
        pass

    def draw_card(self):
        # Add code to draw a card from the deck
        pass

    def add_card(self, card):
        # Add code to add a card to the deck
        pass

    def remove_card(self, card):
        # Add code to remove a card from the deck
        pass