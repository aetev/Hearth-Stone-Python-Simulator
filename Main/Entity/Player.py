from dataclasses import dataclass  # import the dataclass decorator
from CardLib.CardBase import Card  # import the Card class


@dataclass
class PlayerClass:
    """
    Player class
    """

    board: list[Card] = None
    deck: list[Card] = None
    hand: list[Card] = None
    max_health: int = 30
    health: int = 30
