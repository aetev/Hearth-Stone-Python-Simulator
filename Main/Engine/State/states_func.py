"""
function deffinitions for the states module
"""

from Main.Engine.State.states_base import Strategy  # This is the only import needed
from Main.Entity.game_state import GameState  # This is the only import needed
from Main.Engine.Effects.effect_func import DrawCard
from Main.Engine.Targeting.target_func import FreindlyHero, EnemyHero


class Mulligan(Strategy):
    """
    This class is used to determine the mulligan strategy of a player.
    """

    def execute(self, game_state: GameState, action_num: int) -> None:
        """
        This method is used to execute the mulligan strategy of a player.
        """
        draw = DrawCard(FreindlyHero, 3) + DrawCard(EnemyHero, 4)
        draw.execute(game_state)
