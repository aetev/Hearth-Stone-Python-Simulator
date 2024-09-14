"""
This file is used to determine the effects of a card.
"""

from abc import ABC, abstractmethod
from typing import List
from Main.Engine.Targeting.target_base import Target
from Main.Entity.game_state import GameState


class Effect(ABC):

    @abstractmethod
    def execute(self, game_state: GameState) -> None:
        """
        This method is used to execute the effect of a card.
        """

    def __add__(self, other: "Effect") -> "ChainedEffect":
        return ChainedEffect([self, other])


class ChainedEffect(Effect):
    def __init__(self, effects: List[Effect]):
        self.effects = effects

    def execute(self, game_state: GameState) -> None:
        for effect in self.effects:
            effect.execute(game_state)
