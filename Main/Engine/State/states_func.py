"""
function deffinitions for the states module
"""

from Main.Engine.State.states_base import Strategy  # This is the only import needed
from Main.Entity.game_state import GameState  # This is the only import needed


class Mulligan(Strategy):
    """
    This class is used to determine the mulligan strategy of a player.
    """

    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the mulligan strategy of a player.
        """
