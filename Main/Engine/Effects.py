"""
This file is used to determine the effects of a card.
"""

from Main.Engine.target_func import Target
from Main.Entity.game_state import GameState


class Effect:
    """
    This class is used to determine the effect of a card.
    """

    def __init__(self, target: Target, amount: int) -> None:
        """
        This method is used to initialize the effect of a card
        """
        self.target = target
        self.amount = amount

    def exectute(self, game_state: GameState) -> None:
        """
        This method is used to execute the effect of a card.
        """


class Damage(Effect):
    """
    This class is used to determine the damage effect of a card.
    """

    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the damage effect of a card.
        """
        target = self.target.get_target(game_state)
        target.health -= self.amount
