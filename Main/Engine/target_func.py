"""
This module is used to determine the target of an effect.
"""

from Main.Entity.game_state import GameState  # This is the only import needed


class Target:
    """
    This class is used to determine the target of an effect.
    """

    def get_target(self, game_state: GameState) -> object:
        """
        This method is used to get the target of an effect.
        """


class FreindlyHero(Target):
    """
    This class targets the hero that played it.
    """

    def get_target(self, game_state: GameState) -> object:
        return game_state.player_1
