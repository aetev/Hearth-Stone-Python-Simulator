"""
this file contains the GameState class
"""

from dataclasses import dataclass  # import the dataclass decorator
from Main.Entity.player import PlayerClass  # import the Player class


@dataclass
class GameState:
    """
    GameState class
    """

    player_1: PlayerClass
    player_2: PlayerClass
    active_player: None
