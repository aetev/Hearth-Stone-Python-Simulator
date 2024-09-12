"""
this file contains the GameState class
"""

from dataclasses import dataclass  # import the dataclass decorator
from Main.Entity.player_base import Player  # import the Player class


@dataclass
class GameState:
    """
    GameState class
    """

    player_1: Player
    player_2: Player
    active_player: None
