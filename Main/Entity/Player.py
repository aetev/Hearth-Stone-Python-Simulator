from .Deck import Deck

class Player:
    def __init__(self, Deck: Deck):
        self.health = 30
        self.deck = Deck
        self.hand = None
