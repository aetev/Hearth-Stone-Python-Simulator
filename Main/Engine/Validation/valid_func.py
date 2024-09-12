"""
This file contains the concrete classes for the Chain of Responsibility pattern.
"""

from Main.Engine.Validation.valid_base import ValidationEngine, Handler


class HandValidator(ValidationEngine):
    """
    This class is used to validate the hand of a player.
    """

    def __init__(self) -> None:
        """
        Constructor for the handValidator class.
        """
        self.handlers = [
            ConcreteHandler1,
        ]


class ConcreteHandler1(Handler):
    """
    This class is used to handle requests for the hand validator.
    """

    def handle_request(self, request) -> None:
        if request == "request1":
            print("ConcreteHandler1 handles the request.")
        elif self._successor is not None:
            self._successor.handle_request(request)
