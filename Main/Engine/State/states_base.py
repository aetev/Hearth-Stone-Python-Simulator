"""
base classes for the strategy pattern
"""

from typing import Protocol
from Main.Entity.game_state import GameState


class Strategy(Protocol):
    """
    protocol for the individual strategies
    """

    def __init__(self) -> None:
        pass

    def execute(self, game_state: GameState) -> None:
        """
        method to execute the strategy
        """


class ContextManager(Protocol):
    """
    protocol for the context manager
    """

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def execute_strategy(self, game_state: GameState) -> None:
        """
        method to execute the strategy within the context manager
        """
        return self.strategy.execute(game_state)
