"""
This file is used to specify actual target functions.
"""

from Main.Engine.Targeting.target_base import Target
from Main.Entity.game_state import GameState  # This is the only import needed


class FreindlyHero(Target):
    """
    This class targets the hero that played it.
    """

    def get_target(self, game_state: GameState) -> object:
        return game_state.player_1


class EnemyHero(Target):
    """
    This class targets the hero that played it.
    """

    def get_target(self, game_state: GameState) -> object:
        return game_state.player_2
