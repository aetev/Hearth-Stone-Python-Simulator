"""
This file is used to determine the effects of a card.
"""

from typing import Protocol
from typing import List
from Main.Engine.Targeting.target_base import Target
from Main.Entity.game_state import GameState


class Effect(Protocol):
    """
    This protocol is used to define the effect of a card.
    """

    def __init__(self, target: Target, *args) -> None:
        """
        This method is used to initialize the effect of a card.
        """
        self.target = target()
        self.args = args

    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the effect of a card.
        """
        if isinstance(self, list):
            for effect in self:
                effect.execute(game_state)
        else:
            self._execute(game_state)

    def __add__(self, other: "Effect") -> List["Effect"]:
        """
        This method allows chaining of effects using the + operator.
        """
        return [self, other]
