"""
This module is used to determine the target of an effect.
"""

from typing import Protocol
from Main.Entity.game_state import GameState  # This is the only import needed


class Target(Protocol):
    """
    This class is used to determine the target of an effect.
    """

    def __init__(self):
        pass

    def get_target(self, game_state: GameState) -> object:
        """
        This method is used to get the target of an effect.
        """
