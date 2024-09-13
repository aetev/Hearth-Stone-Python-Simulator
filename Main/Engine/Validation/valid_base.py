"""
Chain of Responsibility Design Pattern
"""

from typing import Protocol, List, Optional
from Main.Entity.game_state import GameState


class Handler(Protocol):
    """
    Protocol for handling requests.
    """

    def __init__(self, successor: Optional["Handler"] = None) -> None:
        """
        Constructor for the Handler class.
        args:
        """
        self._successor = successor

    def handle_request(self, game_state: GameState) -> bool:
        """
        Method for handling requests.
        """


class ValidationEngine(Protocol):
    """
    Protocol for the validation engine.
    """

    def __init__(self) -> None:
        """
        Constructor for the ValidationEngine class.
        """
        self.handlers: List[Handler] = []

    def validate(self, game_state: GameState) -> bool:
        """
        Method for validating requests.
        Returns True if all handlers validate the request, otherwise False.
        """
        for handler in self.handlers:
            if not handler.handle_request(game_state):
                return False
        return True
