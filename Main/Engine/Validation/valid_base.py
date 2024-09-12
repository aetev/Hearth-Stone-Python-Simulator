"""
Chain of Responsibility Design Pattern
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    """
    Abstract class for handling requests.
    """

    @abstractmethod
    def __init__(self, successor=None) -> None:
        """
        Constructor for the Handler class.
        args:
        """
        self._successor = successor

    def handle_request(self, request) -> None:
        """
        Abstract method for handling requests.
        """


class ValidationEngine(ABC):
    """
    Abstract class for the validation engine.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Constructor for the ValidationEngine class.
        """
        self.handlers = []

    @abstractmethod
    def validate(self, request) -> None:
        """
        Method for validating requests.
        """
        for handler in self.handlers:
            handler.handle_request(request)
