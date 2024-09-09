from dataclasses import dataclass
from CardLib.CardBase import Card


@dataclass
class Player:
    board: list[Card] = None
    deck: list[Card] = None
    hand: list[Card] = None
    max_health: int = 30
    health: int = 30
