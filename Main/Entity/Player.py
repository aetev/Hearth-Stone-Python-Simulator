from dataclasses import dataclass


@dataclass
class Player:
    health = 30
    deck = None
    hand = None
